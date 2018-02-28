from flask import Flask, abort
from flask import request
from flask import jsonify
from flask_cors import CORS
from Core.sender import Sender
from flask import render_template, render_template_string ,request
import requests
from Core.NLP.NLP import NLP
from Core.checker import *
from Core.RECOMMENDER import *


app = Flask(__name__)

############################################## allow access ###################################################

cors = CORS(app, resources={r"/main/*" : {"origins": "*"}})
cors1 = CORS(app, resources={r"/tv/*" : {"origins": "*"}})
cors2 = CORS(app, resources={r"/conditioner/*" : {"origins": "*"}})

###################################### instances and variables #################################################



clientName = 'user'
TOPIC = 'PI'
EAR = NLP()
send = Sender()



def recmmend(mgenra):
    Movies = pd.read_csv('Core/DataSets/movie_metadata.csv')
    gn = MoviesGenra[mgenra]
    A = RECOMMENDER(Movies, [gn,5])
    opt = A.Model(A.listOfValues)
    recomendedItem = A.outPutHandling(opt)
    return recomendedItem



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



                                    ################ EAR  #################
    EAR.execute(message)
    if EAR.information['Type'] == 'movie':
        genra = EAR.information['Category']
        movie = recmmend(genra)
        return jsonify({'message': 'Here is your Movie : '+movie}), 200




                                    ################ Hardware  #################

    send.Conect(clientName)
    send.send(clientName , TOPIC , message)
    send.disconnect(clientName)


    # Call reciever to get the current state





                                    ################ Mouth  #################
    # NLG TO generate response







                                    ################ Memory  #################
    # save the data in db








    return jsonify({'message': EAR.information}), 200

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
