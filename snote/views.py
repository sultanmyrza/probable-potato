import json

from django.http.response import HttpResponse
from django.shortcuts import render

from snote.models import Node

def home(request):
    nodes = Node.objects.all()
    json_nodes = []
    for node in nodes:
        group = ''
        if not node.is_child_node():
            group = 'diamonds'
        json_nodes.append({
            'id': node.id,
            'label': '{0}. {1}'.format(node.id, node.title),
            'summary': node.summary,
            'group': group
        })

    edges = []
    root_nodes = Node.objects.root_nodes()
    for node in root_nodes:
        print node.title, node.get_edges()
        for children in node.get_edges():
            print children
            for edge in children[1:]:
                edge = {
                    'from': children[0],
                    'to': edge,
                }
                print 'edge', edge
                edges.append(edge)

    context = {
        'nodes': json.dumps(json_nodes),
        'edges': json.dumps(edges),
    }
    return render(request, 'snote/home.html', context)


def detail(request, node_id):
    node = Node.objects.get(id=node_id)
    return HttpResponse(node.summary, content_type='text/plain')

def notes(request, node_id):
    node = Node.objects.get(id=node_id)
    notes = node.note_set.all()
    notes_html = ''
    for note in notes:
        notes_html += ('<pre>')
        notes_html += (note.content)
        notes_html += ('</pre>')
    return HttpResponse(notes_html)