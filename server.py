
import json

import eventlet
import socketio

from features.fusion_calcs.controller import on_client_state_changed

PORT = 3001
sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio, static_files={
    '/meta.json': { 'filename': 'static/meta.json'},
    '/market.png': { 'filename': 'static/market.png'}
})


@sio.on('client-state-changed')
def on_event(sid, data):
    on_client_state_changed(sio, sid, json.loads(data))


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', PORT)), app)
