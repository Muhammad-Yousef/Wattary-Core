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

### Importing the Eye Module ###
from Core.Eye import eye as checker


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
cors4 = CORS(app, resources={r"/signup/*": {"origins": "*"}})

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







################################################# SignUp #######################################################


@app.route('/signup', methods=['POST'])
def SignUp():
    if not request.json or not 'PhotoUrl' in request.json and 'UserName' in request.json:
        abort(400)
        '''
        pull the user data from the json requests
        - Username
        - image URL
        - 4 digit pin code (Not Confirmed)

        '''

    # invoke the Memory and Eye Function
    imageURL = request.json['PhotoUrl']
    userName = request.json['UserName']

    # Adding new User in the database with his username and his image
    if checker.register(userName, imageURL) == 101:
        return jsonify({'response': "Operation succeeded. New User added to database"}), 200
    # Case 2 that if the image doesn't exist (URL Error)
    elif checker.register(userName, imageURL) == 102:
        return jsonify({'response': "Cannot read the picture (not Exist)."}), 102
    # Case 3: If the image isn't contain any faces
    elif checker.register(userName, imageURL) == 103:
        return jsonify({'response': "Cannot find any faces in the picture (retake the picture)."}), 103
    # Case 4: If the user image and username is already exist
    elif checker.register(userName, imageURL) == 104:
        return jsonify({'response': "This user is exist."}), 104
    # Case 5: DataBase connection error or adding error.
    elif checker.register(userName, imageURL) == 105:
        return jsonify({'response': "There's a problem in the database."}), 105


################################################# SignIn #######################################################

@app.route('/signin', methods=['POST'])
def SignIn():
    if not request.json or not 'PhotoUrl' in request.json:
        abort(400)

    # invoke the Memory and Eye Function
    imageURL = request.json['PhotoUrl']

    # Login with the image of the user
    code, userID = checker.login(imageURL)
    if code == 201:
        return jsonify({'response': "Operation succeeded." + userID}), 200
    # # Case 2 that if the image doesn't exist (URL Error)
    # elif checker.login(imageURL) == 202:
    #     return jsonify({'response': "Cannot read the picture (not Exist)."}), 202
    # # Case 3: If the image isn't contain any faces
    # elif checker.login(imageURL) == 203:
    #     return jsonify({'response': "Cannot find any faces in the picture (retake the picture)."}), 203
    # # Case 5: DataBase connection error or adding error.
    # elif checker.login(imageURL) == 205:
    #     return jsonify({'response': "There's a problem in the database."}), 205
    # # Case 6: If Wattary doesn't recognize this person or he is not a user.
    # elif checker.login(imageURL) == 206:
    #     return jsonify({'response': "Cannot recognize this person."}), 206

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
