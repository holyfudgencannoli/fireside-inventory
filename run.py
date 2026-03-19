import socketio

from app import create_app

app, socketio = create_app()

if __name__ == '__main__':
    # Use eventlet for WebSocket support
    import eventlet
    import eventlet.wsgi
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)

