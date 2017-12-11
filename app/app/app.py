#########################################
#############                  ##########
############# Testing SocketIO ##########
#############     Localy       ##########
#########################################
from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

hi = ""

@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)
	hi = msg





@app.route('/')
def index():
	return hi


if __name__ == '__main__':
	socketio.run(app,host='0.0.0.0',port=80)
