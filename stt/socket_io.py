import os
from flask_socketio import emit
from flask import request
from .recognizer import STTRecognizer

# Build model path relative to this file
MODEL_PATH = os.path.join(os.path.dirname(__file__), '.', 'am_models', 'vosk-model-small-en-us-0.15')
MODEL_PATH = os.path.normpath(MODEL_PATH)
recognizer_manager = STTRecognizer(MODEL_PATH)
clients = {}  # store recognizers per connection

def connect(sid):
    clients[sid] = recognizer_manager.create_recognizer()
    print(f"Client {sid} connected")

def disconnect(sid):
    clients.pop(sid, None)
    print(f"Client {sid} disconnected")

def receive_audio(sid, audio_bytes):
    rec = clients[sid]
    result = recognizer_manager.accept_audio(rec, audio_bytes)
    emit("result", {"type": "partial" if "partial" in result else "final", "text": result.get("text", "")}, to=sid)