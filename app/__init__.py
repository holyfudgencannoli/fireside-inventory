from math import log
import os

from flask import Flask, request
from flask_cors import CORS
from config import Config
from db import Base, engine
from flask_socketio import SocketIO
from stt import socket_io as stt_socket
from flask_socketio import SocketIO, emit
from flask import request

from stt.recognizer import STTRecognizer

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "supersecret"
    app.config.from_object(Config)
    CORS(app, resources={r"/api/*": {"origins": ["http://localhost:8081", "http://localhost"]}}, supports_credentials=True)

    import models

    Base.metadata.create_all(bind=engine)
    
    socketio = SocketIO(app, cors_allowed_origins="*", logger=True, engineio_logger=True)
    
    @socketio.on("connect")
    def handle_connect():
        sid = request.sid
        stt_socket.connect(sid)

    @socketio.on("disconnect")
    def handle_disconnect():
        sid = request.sid
        stt_socket.disconnect(sid)

    @socketio.on("audio")
    def handle_audio(audio_bytes):
        sid = request.sid
        stt_socket.receive_audio(sid, audio_bytes)

        emit("result", {
            "type": "partial" if "partial" in result else "final",
            "text": result.get("text", "")
        }, to=sid)

    return app, socketio