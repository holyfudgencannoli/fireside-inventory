import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("connected")

@sio.event
def disconnect():
    print("disconnected")

@sio.event
def on_audio(data):
    print("Received audio:", data)

sio.connect("http://10.0.0.45:5000")
sio.on("audio", on_audio)
sio.wait()
