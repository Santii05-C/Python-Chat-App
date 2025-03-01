from flask import Flask,render_template,request
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
socketio = SocketIO(app)

# python dict. Store connected users. Key is socket id, value is username and avatarUrl 
users = {}

@app.route('/')
def index():
    return render_template('index.html')

# we're listening for the connect event
@socketio.on("connect")
def handle_connect():
    username = f"User_{random.randint(1000,9999)}"
    gender = random.choice(["girl","boy"])
    avatar_url = f" https://avatar.iran.liara.run/public/{gender}?username={username}"
    
    users[request.sid] = { "username":username,"avatar":avatar_url}
    
    emit("user_joined", {"username":username,"avatar":avatar_url},broadcast=True)


if __name__ == "__main__":
    socketio.run (app)