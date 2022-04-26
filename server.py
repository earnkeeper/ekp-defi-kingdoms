import json
import time

import eventlet
import socketio

PORT = 3001

print("Server listening on Port " + str(PORT))

sio = socketio.Server(cors_allowed_origins = '*')
app = socketio.WSGIApp(sio)

def emit_menu(sid, id, title, nav_link, icon):
    menu = {"id": id, "title": title, "navLink": nav_link, "icon": icon};
    message = { "layers": [{ "id": "menu-%s" % (id), "collectionName": "menus", "set": [menu], "timestamp": int(time.time()) }] }
    sio.emit('add-layers', json.dumps(message), room = sid)

def emit_page(sid, id, element):
    page = { "id": id, "element": element };
    message = { "layers": [{ "id": "page-%s" % (id), "collectionName": "pages", "set": [page], "timestamp": int(time.time()) }] }
    sio.emit('add-layers', json.dumps(message), room = sid)

@sio.on('client-state-changed')
def on_event(sid, data):
    emit_menu(sid, 'gameinfo', 'Game Info', 'gameinfo', 'cil-info')
    element = { "_type": "Span", "props":  { "className": "font-medium-3", "content": "Game Info"} }
    emit_page(sid, "gameinfo", element)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', PORT)), app)

