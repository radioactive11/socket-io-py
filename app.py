import socketio


sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': './public/'
})


@sio.event
def connect(sid, environ):
    """
    sid is session id which is created by socket-io when a client connects
    environ is a dictionary which has all the details from the client request
    """
    print(f"[CONNECTED] {sid}")
    

    

@sio.event
def disconnect(sid):
    print(f"[DISCONNECTED] {sid}")

# Use a WSGI webserver like gunicron to run the server
