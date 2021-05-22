import socketio


sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': './public/'
})


def task(sid):
    sio.sleep(3)
    result = sio.call('mult', {'numbers': [3, 4]}, to=sid)
    print(result)



@sio.event
def connect(sid, environ):
    """
    sid is session id which is created by socket-io when a client connects
    environ is a dictionary which has all the details from the client request
    """
    print(f"[CONNECTED] {sid}")
    sio.start_background_task(task, sid)

@sio.event
def disconnect(sid):
    print(f"[DISCONNECTED] {sid}")


@sio.event
def sum(sid, data):
    result = data['numbers'][0] + data['numbers'][1]
    # sio.emit('sum_result', {'result': result}, to=sid)
    return {'result': result}



# Use a WSGI webserver like gunicron to run the server
