from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
# 解决跨域
cors = CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/")
def list_users():
    return "hello"


@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)


if __name__ == '__main__':
    socketio.run(app, debug=True)
