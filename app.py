from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dein-geheimes-schlüssel'  # Ersetze durch einen sicheren Schlüssel
socketio = SocketIO(app, cors_allowed_origins="*")  # Erlaube alle Ursprünge (für die Entwicklung)

# Rest des Codes bleibt gleich

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
    socketio.run(app, debug=True)
