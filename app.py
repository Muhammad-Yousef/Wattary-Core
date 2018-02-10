##################################### Imorting the Modules  ###########################################


from flask import Flask
from flask_socketio import SocketIO, send
from Core.sender import Sender


#######################################################################################################
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)


clientName = 'user'
TOPIC = 'PI'


#  an example of  switch the light on
def lightOn(message):
	send = Sender()
	send.Conect(clientName)
	send.send(clientName , TOPIC , message)
	send.disconnect(clientName)


@socketio.on('message')
def handleMessage(msg):
	lightOn(int(msg))




@app.route('/')
def homepage():


    return """
    <h1>Hello Wattary</h1>

  
    """



if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)

