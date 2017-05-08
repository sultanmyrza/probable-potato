from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import DraggableMPTTAdmin
from snote.models import Node, Note

class NoteInline(admin.TabularInline):
    model = Note
    extra = 0
    # formset = NoteFormSet


class NodeDraggableMPTTAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'summary')
    # list_display_links = ('',)
    inlines = [
        NoteInline,
    ]

admin.site.register(Node, NodeDraggableMPTTAdmin)