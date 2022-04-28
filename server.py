import json
import time

import eventlet
import socketio
from fusion_calcs_documents import fusionCalcDocuments

from fusion_calcs_element import fusionCalcsElement


PORT = 3001

print("Server listening on Port " + str(PORT))

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)


def emit_menu(sid, id, title, nav_link, icon):
    menu = {"id": id, "title": title, "navLink": nav_link, "icon": icon}
    message = {"layers": [{"id": "menu-%s" % (id), "collectionName": "menus", "set": [
        menu], "timestamp": int(time.time())}]}
    sio.emit('add-layers', json.dumps(message), room=sid)


def emit_page(sid, id, element):
    page = {"id": id, "element": element}
    message = {"layers": [{"id": f'page-{id}', "collectionName": "pages", "set": [
        page], "timestamp": int(time.time())}]}
    sio.emit('add-layers', json.dumps(message), room=sid)


def emit_documents(sid, collection_name, documents):
    message = {
        "layers": [
            {
                "id": collection_name,
                "collectionName": collection_name,
                "set": documents,
                "timestamp": int(time.time())
            }
        ]
    }
    sio.emit('add-layers', json.dumps(message), room=sid)


@sio.on('client-state-changed')
def on_event(sid, data):
    emit_menu(sid, 'herobox', 'Hero Box', 'herobox', 'box')
    emit_page(sid, "herobox", fusionCalcsElement())
    emit_documents(sid, "fusioncalcs", fusionCalcDocuments())


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', PORT)), app)
