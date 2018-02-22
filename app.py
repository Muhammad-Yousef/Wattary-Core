from flask import Flask, abort
from flask import request
from flask import jsonify
from flask_cors import CORS
from Core.sender import Sender
from flask import render_template, render_template_string ,request
import requests


app = Flask(__name__)

############################################## allow access ###################################################

cors = CORS(app, resources={r"/main/*" : {"origins": "*"}})
cors1 = CORS(app, resources={r"/tv/*" : {"origins": "*"}})
cors2 = CORS(app, resources={r"/conditioner/*" : {"origins": "*"}})

###############################################################################################################



clientName = 'user'
TOPIC = 'PI'



################################################# weather API Function  ############################################


def get_temperature(city):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+',eg&appid= ')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    temp_c = temp_k -  273.15
    return temp_c



################################################# Main API  #######################################################

@app.route('/main', methods=['POST'])
def analyze_data():
    if not request.json or not 'message' in request.json:
        abort(400)
    message = request.json['message']

    # NLP processing

    send = Sender()
    send.Conect(clientName)
    send.send(clientName , TOPIC , message)
    send.disconnect(clientName)


    print(get_temperature('alexandria')) # this line to test the weather api only


    # Call reciever to get the current state


    # NLG TO generate response


    # save the data in db

    return jsonify({'message': message}), 200

################################################# tv API  #######################################################

@app.route('/tv', methods=['POST'])
def remote_control():
    if not request.json or not 'channel' in request.json:
        abort(400)
    channel = request.json['channel']



    send = Sender()
    send.Conect(clientName)
    send.send(clientName , TOPIC , channel)
    send.disconnect(clientName)

    # Call reciever to get the current state


    return jsonify({'response': "CH.NO " + channel}), 200



################################################# Air conditioner  API  #######################################################

@app.route('/conditioner', methods=['POST'])
def air_conditioner():
    if not request.json or not 'command' in request.json:
        abort(400)
    command = request.json['command']



    send = Sender()
    send.Conect(clientName)
    send.send(clientName , TOPIC , command)
    send.disconnect(clientName)

    # Call reciever to get the current state


    return jsonify({'response': "The command you choose is " + command}), 200




@app.route('/')
def homepage():


    return render_template('index.html')




if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)
