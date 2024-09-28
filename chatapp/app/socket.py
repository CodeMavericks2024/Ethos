from flask_socketio import send, join_room
from app import socketio, db
from app.models import Message

@socketio.on('send_message')
def handle_message(data):
    message = Message(sender_id=data['sender_id'], receiver_id=data['receiver_id'], message_text=data['message'])
    db.session.add(message)
    db.session.commit()
    send(data, room=f"user_{data['receiver_id']}")

@socketio.on('join')
def on_join(data):
    room = f"user_{data['user_id']}"
    join_room(room)
    send(f"User {data['user_id']} has joined the room.", room=room)

