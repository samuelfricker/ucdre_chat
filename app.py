from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback-schlüssel-für-lokale-tests')

# Socket.IO mit gevent als async_mode
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='gevent')

# In-memory message store
messages = []
participants = set()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('join')
def handle_join(data):
    username = data['username']
    participants.add(username)
    emit('user_joined', {'username': username}, broadcast=True)
    emit('update_participants', {'participants': list(participants)})

@socketio.on('leave')
def handle_leave(data):
    username = data['username']
    participants.discard(username)
    emit('user_left', {'username': username}, broadcast=True)
    emit('update_participants', {'participants': list(participants)})

@socketio.on('send_message')
def handle_message(data):
    message = {
        'sender': data['sender'],
        'text': data['text'],
        'timestamp': data['timestamp']
    }
    messages.append(message)
    emit('new_message', message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
