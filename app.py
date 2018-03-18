from flask import Flask, abort
from flask import request
from flask import jsonify
from flask_cors import CORS
from Core.sender import Sender
from flask import render_template, render_template_string, request
import requests
from Core.NLP.NLP import NLP
from Core.checker import *
from Core.RECOMMENDER import *
from Core.Mouth.Mouth import *

### Importing the Database Module ###
from Core.Memory import memory
import logging


############################################## Configurations ############################################

app = Flask(__name__)
app.config['DEBUG'] = True

        ### Database Configuration ###
# POSTGRES = {
#     'user': 'postgres',
#     'pw': 'password',
#     'db': 'my_database',
#     'host': 'localhost',
#     'port': '5432',
# }
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
# %(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
# db.connect


############################################## allow access ###################################################

cors = CORS(app, resources={r"/main/*": {"origins": "*"}})
cors1 = CORS(app, resources={r"/tv/*": {"origins": "*"}})
cors2 = CORS(app, resources={r"/conditioner/*": {"origins": "*"}})
cors3 = CORS(app, resources={r"/signin/*": {"origins": "*"}})

###################################### instances and variables #################################################


clientName = 'user'
TOPIC = 'pi'
# EAR = NLP()
send = Sender()
# Mouth = Mouth()
# send = Sender()

### Database instance ###
db = memory


def recommend(mgenra):
    Movies = pd.read_csv('Core/DataSets/movie_metadata.csv')
    gn = MoviesGenra[mgenra]
    A = RECOMMENDER(Movies, [gn, 5])
    opt = A.Model(A.listOfValues)
    recomendedItem = A.outPutHandling(opt)
    return recomendedItem


################################################# weather API Function  ############################################


def get_temperature(city):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + ',eg&appid= ')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    temp_c = temp_k - 273.15
    return temp_c


################################################# SignIn #######################################################

@app.route('/signin', methods=['POST'])
def SignIn():
    if not request.json or not 'data' in request.json:
        abort(400)
        '''
         pull the user data from the json requests
            - Username
            - image URL
            - 4 digit pin code (Not Confirmed)

        '''

        # invoke the Memory and Eye Function

    return jsonify({'response': "Done"}), 200


################################################# Main API  #######################################################

@app.route('/main', methods=['POST'])
def analyze_data():
    if not request.json or not 'message' in request.json:
        abort(400)
    message = request.json['message']

    EAR = NLP()
    Mou = Mouth()
    ################ EAR  #################
    EAR.execute(message)
    try:
        if EAR.information['Type'] == 'movie':
            genra = EAR.information['Category']
            movie = recommend(genra)
            return jsonify({'message': 'Here is your Movie : ' + movie}), 200
    except (RuntimeError, TypeError, NameError, KeyError):
        pass

        ################# Light Cycle ##################
    try:
        if EAR.information['Appliance'] == 'light' and EAR.information['State'] == 'on':
            code = lightCodeON[EAR.information['Location']]
            print(code)

            send.Conect(clientName)
            send.send(clientName, TOPIC, code)
            send.disconnect(clientName)
        elif EAR.information['Appliance'] == 'light' and EAR.information['State'] == 'off':
            code = lightCodeOff[EAR.information['Location']]

            send.Conect(clientName)
            send.send(clientName, TOPIC, code)
            send.disconnect(clientName)
    except (RuntimeError, TypeError, NameError, KeyError):
        pass


        # save

    ########################################       tv Cycle                 ##########################################

    try:
        if EAR.information['Appliance'] == 'television':
            code = tvCode[EAR.information['State']]
            print(code)

            send.Conect(clientName)
            send.send(clientName, TOPIC, code)
            send.disconnect(clientName)
    except (RuntimeError, TypeError, NameError, KeyError):
        pass

    #######################################    coffee machine Cycle   #########################################


    try:
        if EAR.information['Appliance'] == 'coffee machine':
            code = coffeeCode[EAR.information['State']]
            print(code)

            send.Conect(clientName)
            send.send(clientName, TOPIC, code)
            send.disconnect(clientName)
    except (RuntimeError, TypeError, NameError, KeyError):
        pass

        # Call reciever to get the current state









        ################ Memory  #################
        # save the data in db

        ### Testing data ###
        # code = db.insertValues('air_con_DS', {'o_val': 33, 'in_val': 22})
        # if code == 202:
        #     logging.warning('the user_id is not exist.')
        # elif code == 203:
        #     logging.warning('Failed to connect to the Database.')
        # elif code != 201:
        #     logging.warning('unrecognized code: ' + code)



        ################ Mouth  #################

    Mou.speak(EAR.intent, EAR.tense)
    return jsonify({'message': Mou.respone}), 200


################################################# tv API  #######################################################

@app.route('/tv', methods=['POST'])
def remote_control():
    if not request.json or not 'channel' in request.json:
        abort(400)
    channel = request.json['channel']

    send = Sender()
    send.Conect(clientName)
    send.send(clientName, TOPIC, channel)
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
    send.send(clientName, TOPIC, command)
    send.disconnect(clientName)

    # Call reciever to get the current state


    return jsonify({'response': "The command you choose is " + command}), 200


@app.route('/')
def homepage():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
