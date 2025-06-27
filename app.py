from flask import Flask, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'  # You can customize this

socketio = SocketIO(app, cors_allowed_origins="*")  # Allow CORS for all origins

@socketio.on('connect')
def handle_connect():
    print("Client connected:", request.remote_addr)

@socketio.on('message')
def handle_message(data):
    print("Message received:", data)
    socketio.send(f"Echo: {data}")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=10000)
