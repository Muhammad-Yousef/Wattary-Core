from flask import Flask, abort
from flask import request
from flask import jsonify
from flask_cors import CORS
import sys
sys.path.append('./Core')
sys.path.append('./Core/NLP')
sys.path.append('./Core/Mouth')
sys.path.append('./Core/Eye')
from sender import Sender
from flask import render_template, render_template_string, request
import requests
from NLP import NLP
from checker import *
from RECOMMENDER import *
from Mouth import *
import datetime
from AirCond import *
### Importing the Database Module ###
from Memory import memory
import logging

### Importing the Eye Module ###
import eye as checker


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
cors5 = CORS(app, resources={r"/signup/web*": {"origins": "*"}})
cors6 = CORS(app, resources={r"/signin/web*": {"origins": "*"}})
cors7 = CORS(app, resources={r"/learn*": {"origins": "*"}})
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

##########################################################################################################
@app.route('/learn', methods=['POST'])
def Learn():
    if not request.json or not 'hours' in request.json and 'minutes' in request.json:
        abort(400)
    DateTime=datetime.datetime.now()
    Interior_Value=30
    Exterior_Value=35
    obj.Model_fitting(DateTime.date().toordinal(),DateTime.hour,DateTime.minute,Interior_Value,Exterior_Value)
    res = obj.display()
    return jsonify({'response': res}), 200

################################################# weather API Function  ############################################


def get_temperature(city):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + ',eg&appid= ')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    temp_c = temp_k - 273.15
    return temp_c







################################################# SignUp #######################################################
@app.route('/signup/web', methods=['POST'])
def SignUpWeb():
    if not request.json or not 'password' in request.json and 'UserName' in request.json and 'email' in request.json:
        abort(400)

    username = request.json['UserName']
    password = request.json['password']
    email = request.json['email']
    code = checker.register_password(username,password,email)
    print(code)
    if code == 101:
        return jsonify({'response': "Operation succeeded. New User added to database"}), 200
    elif code == 104:
        return jsonify({'response': "This user is exist."}), 200

    elif code == 105:
        return jsonify({'response': "There's a problem in the database."}), 105









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

    code = checker.register(userName, imageURL)
    # Adding new User in the database with his username and his image
    # Case 1: this means the operation succeeded.
    if code == 101:
        return jsonify({'response': "Operation succeeded. New User added to database"}), 200
    # Case 2: this means that I can not read the picture (not Exist).
    elif code == 102:
        return jsonify({'response': "Cannot read the picture (not Exist)."}), 102
    # Case 3: this means that I can not find any faces in the picture (retake a picture)
    elif code == 103:
        return jsonify({'response': "Cannot find any faces in the picture (retake the picture)."}), 103
    # Case 4: this means that the user is exist.
    elif code == 104:
        return jsonify({'response': "This user is exist."}), 104
    # Case 5: this means a memory (database) error.
    elif code == 105:
        return jsonify({'response': "There's a problem in the database."}), 105


################################################# SignIn #######################################################

@app.route('/signin/web', methods=['POST'])
def SignInWeb():
    if not request.json or not 'password' in request.json and 'UserName' in request.json:
        abort(400)


    username = request.json['UserName']
    password = request.json['password']
    code,uname = checker.login_password(username,password)
    if code == 501:
        return jsonify({'response': "welcome " + uname }), 200
    # Case 2: this means that I can not read the picture (not Exist).
    else:
        return jsonify({'respone':"user name or password is incorrect"}), 209





@app.route('/signin', methods=['POST'])
def SignIn():
    if not request.json or not 'PhotoUrl' in request.json:
        abort(400)

    # invoke the Memory and Eye Function
    imageURL = request.json['PhotoUrl']

    # Login with the image of the user
    code, userID = checker.login(imageURL)
    # Case 1 this mean that the user is exist.
    if code == 201:
        return jsonify({'response': "Operation succeeded." + userID}), 200
    # Case 2 this means that I can not read the picture (not Exist).
    elif code == 202:
        return jsonify({'response': "Cannot read the picture (not Exist)."}), 202
    # Case 3: this means that I can not find any faces in the picture (retake a picture).
    elif code == 203:
        return jsonify({'response': "Cannot find any faces in the picture (retake the picture)."}), 203
    # Case 4: this means that I can not recognize this person.
    elif code == 204:
        return jsonify({'response': "I can not recognize this person."}), 204

################################################# Main API  #######################################################

@app.route('/main', methods=['POST'])
def analyze_data():
    if not request.json or not 'message' in request.json:
        abort(400)
    message = request.json['message']

    EAR = NLP()
    Mou = Mouth()
    ################ RECOMMENDER  #################
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
            print(Devices[EAR.information['Location']])
            if Devices[EAR.information['Location']] == '1':
                return jsonify({'message': "it's already on "}), 207

            send.Conect(clientName)
            send.send(clientName, TOPIC, code)
            send.disconnect(clientName)
            Devices[EAR.information['Location']] = '1'
            print(Devices[EAR.information['Location']])
        elif EAR.information['Appliance'] == 'light' and EAR.information['State'] == 'off':
            code = lightCodeOff[EAR.information['Location']]
            if Devices[EAR.information['Location']] == '0':
                return jsonify({'message': "it's already off "}), 207
            send.Conect(clientName)
            send.send(clientName, TOPIC, code)
            send.disconnect(clientName)
            Devices[EAR.information['Location']] = '0'
    except (RuntimeError, TypeError, NameError, KeyError):
        pass


        # save

    ########################################       tv Cycle                 ##########################################

    try:
        if EAR.information['Appliance'] == 'television':
            code = tvCode[EAR.information['State']]
            print(code)
            print(Devices["tv"])

            if code == '17' and Devices["tv"] == '1':
                return jsonify({'message': "it's already on "}), 207

            if code == '18' and Devices["tv"] == '0':
                return jsonify({'message': "it's already off "}), 207

            send.Conect(clientName)
            send.send(clientName, TOPIC, code)
            send.disconnect(clientName)

            if code == '17':
                Devices["tv"] = '1'
            if code == '18':
                Devices["tv"] = '0'

    except (RuntimeError, TypeError, NameError, KeyError):
        pass

    #######################################    coffee machine Cycle   #########################################


    try:
        if EAR.information['Appliance'] == 'coffee machine':
            code = coffeeCode[EAR.information['State']]
            print(code)
            print(Devices["coffeMachine"])

            if code == '21' and Devices["coffeMachine"] == '1':
                return jsonify({'message': "it's already on "}), 207

            if code == '22' and Devices["coffeMachine"] == '0':
                return jsonify({'message': "it's already off "}), 207

            send.Conect(clientName)
            send.send(clientName, TOPIC, code)
            send.disconnect(clientName)

            if code == '21':
                Devices["coffeMachine"] = '1'
            if code == '22':
                Devices["coffeMachine"] = '0'

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
    app.run(debug=True, use_reloader=True,host='0.0.0.0' )
