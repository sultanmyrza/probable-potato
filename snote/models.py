from __future__ import unicode_literals

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from redactor.fields import RedactorField

edges = []

class Node(MPTTModel):
    title = models.CharField(max_length=50, unique=True)
    summary = models.TextField(null=True, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __unicode__(self):
        return self.title

    def recursion(self):
        global edges
        if not self.is_leaf_node():
            node_edges = [self.id]
            for node in self.get_children():
                node_edges.append(node.id)
                node.recursion()
            edges.append(node_edges)

    def get_edges(self):
        global edges
        edges = []
        self.recursion()
        return edges


class Note(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    content = RedactorField(null=True, blank=True)

    def __unicode__(self):
        return self.content
