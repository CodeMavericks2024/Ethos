from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://chat_user:password@localhost/chat_app'
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
socketio = SocketIO(app)

from app import routes, models, socket

