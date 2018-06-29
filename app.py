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
from LightClassification import *

### Importing the Eye Module ###
import eye as checker



############################################## Configurations ############################################

app = Flask(__name__)
app.config['DEBUG'] = True

Interior_Value = 0
Exterior_Value = 0
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


################################################# weather API Function  ############################################


def get_temperature(city):
    print('321')
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + ',eg&appid=2a3902eb285f33e5150f8f36ec7e81ba')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    temp_c = temp_k - 273.15
    print(temp_c)
    return int(temp_c)
#########################################################################################################################3


def recommend(mgenra):
    Movies = pd.read_csv('Core/DataSets/convertcsv.csv')
    gn = MoviesGenra[mgenra]
    A = RECOMMENDER(Movies, [gn, 5])
    opt = A.Model(A.listOfValues)
    recomendedItem = A.outPutHandling(opt)
    return recomendedItem
######################################  tempretures ######################################################
@app.route('/temp', methods=['POST'])
def getTemp():
    if not request.json or not 'i_val' in request.json and 'e_val' in request.json :
        abort(400)
    global Interior_Value
    Interior_Value = request.json['i_val']
    global Exterior_Value
    Exterior_Value = request.json['e_val']
    return jsonify({'res': 'done'}), 200

######################################  learnin ######################################################
@app.route('/learn', methods=['POST'])
def Learn():
    if not request.json or not 'hours' in request.json and 'minutes' in request.json:
        abort(400)

    print(Interior_Value)  
    print(Exterior_Value)  
    int(Interior_Value)
    int(Exterior_Value)
    DateTime=datetime.datetime.now()
    bedroom = obj1.FitAndPredict(DateTime.date().toordinal(), DateTime.hour, DateTime.minute, int(learn['bedroom']))
    hallway = obj1.FitAndPredict(DateTime.date().toordinal(), DateTime.hour, DateTime.minute, int(learn['hallway']))
    bathroom = obj1.FitAndPredict(DateTime.date().toordinal(),20,DateTime.minute, int(learn['bathroom']))
    obj.Model_fitting(DateTime.date().toordinal(),DateTime.hour,DateTime.minute,Interior_Value,Exterior_Value)
    res = obj.display()
    return jsonify({
        'Air Conditioner': res,
        'bedroom-light':bedroom,
        'hallway-light':hallway,
        'bathroom-light':bathroom
        

    }), 200


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
        return jsonify({'response': "Operation succeeded. New User added to database",
        'state':'101'
        
        }), 200
    elif code == 104:
        return jsonify({'response': "This user is exist.",
        'state':'104'
        }), 200
    elif code == 105:
        return jsonify({'response': "There's a problem in the database.",
        'state':'105'
        }), 200









@app.route('/signup', methods=['POST'])
def SignUp():
    if not request.json and not 'PhotoUrl' in request.json and 'UserName' in request.json and 'password' in request.json:
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
    userpass = request.json['password']

    code = checker.register(userName, imageURL, userpass)
    # Adding new User in the database with his username and his image
    # Case 1: this means the operation succeeded.
    if code == 101:
        return jsonify({'response': "Operation succeeded. New User added to database",
        "code":True
        }), 200
    # Case 2: this means that I can not read the picture (not Exist).
    elif code == 102:
        return jsonify({'response': "Cannot read the picture (not Exist).",
        "code":False
        }), 200
    # Case 3: this means that I can not find any faces in the picture (retake a picture)
    elif code == 103:
        return jsonify({'response': "Cannot find any faces in the picture (retake the picture).",
        "code":False
        }), 200
    # Case 4: this means that the user is exist.
    elif code == 104:
        return jsonify({'response': "This user is exist.",
        "code":False
        }), 200
    # Case 5: this means a memory (database) error.
    elif code == 105:
        return jsonify({'response': "There's a problem in the database.",
        "code":False
        }), 200


################################################# SignIn #######################################################

@app.route('/signin/web', methods=['POST'])
def SignInWeb():
    if not request.json or not 'password' in request.json and 'UserName' in request.json:
        abort(400)


    username = request.json['UserName']
    password = request.json['password']
    code,uname,uid = checker.login_password(username,password)
    if code == 501:
        return jsonify({'response': "welcome " + uname,
        'userName': uname,
        'userID':uid
        
         }), 200
    # Case 2: this means that I can not read the picture (not Exist).
    else:
        return jsonify({'respone':"user name or password is incorrect"}), 200





@app.route('/signin', methods=['POST'])
def SignIn():
    if not request.json or not 'PhotoUrl' in request.json:
        abort(400)

    # invoke the Memory and Eye Function
    imageURL = request.json['PhotoUrl']

    # Login with the image of the user
    code,userName,userID = checker.login(imageURL)
    # Case 1 this mean that the user is exist.
    if code == 201:
        return jsonify({'response': "Operation succeeded." + userID,
        'userName': userName,
        'userID':userID,
        "code":True
        }), 200
    # Case 2 this means that I can not read the picture (not Exist).
    elif code == 202:
        return jsonify({'response': "Cannot read the picture (not Exist).",
        "code":False
        }), 200
    # Case 3: this means that I can not find any faces in the picture (retake a picture).
    elif code == 203:
        return jsonify({'response': "Cannot find any faces in the picture (retake the picture).",
        "code":False
        }), 200
    # Case 4: this means that I can not recognize this person.
    elif code == 204:
        return jsonify({'response': "I can not recognize this person.",
        "code":False
        }), 200

################################################# Main API  #######################################################

@app.route('/main', methods=['POST'])
def analyze_data():
    if not request.json and not 'message' in request.json and 'userID' in request.json:
        abort(400)
    message = request.json['message']
    userid = request.json['userID']
    EAR = NLP()
    Mou = Mouth()
    ################ RECOMMENDER  #################
    EAR.execute(message)
    print(EAR.information)
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

            val = 1
            memory.insertValues('light_DS', {'user_id': int(userid), 'room_num':int(learn[EAR.information['Location']]), 'val':val})

            Mou.speak(EAR.intent, EAR.tense)
            return jsonify({'message': Mou.respone}), 200


            print(Devices[EAR.information['Location']])
        elif EAR.information['Appliance'] == 'light' and EAR.information['State'] == 'off':
            code = lightCodeOff[EAR.information['Location']]
            if Devices[EAR.information['Location']] == '0':
                return jsonify({'message': "it's already off "}), 207
            send.Conect(clientName)
            send.send(clientName, TOPIC, code)
            send.disconnect(clientName)
            Devices[EAR.information['Location']] = '0'

            memory.insertValues('light_DS', {'user_id': int(userid), 'room_num':int(learn[EAR.information['Location']])})


            Mou.speak(EAR.intent, EAR.tense)
            return jsonify({'message': Mou.respone}), 200



    except (RuntimeError, TypeError, NameError, KeyError):
        pass


        # save

    ########################################       tv Cycle                 ##########################################

    try:
        if EAR.information['Appliance'] == 'television':
            code = tvCode[EAR.information['State']]
            print(EAR.information)
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

            Mou.speak(EAR.intent, EAR.tense)
            return jsonify({'message': Mou.respone}), 200


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


            Mou.speak(EAR.intent, EAR.tense)
            return jsonify({'message': Mou.respone}), 200



    except (RuntimeError, TypeError, NameError, KeyError):
        pass

    #######################   air conditioning   ##############################
    try:
        if EAR.information['Appliance'] == 'air conditioner':
            code = airConditioner[EAR.information['State']]
            print(code)
            #print(Devices["airConditioner"])

            if code == '52' and Devices["air conditioner"] == '1':
                return jsonify({'message': "it's already on "}), 207

            if code == '53' and Devices["air conditioner"] == '0':
                return jsonify({'message': "it's already off "}), 207

            send.Conect(clientName)
            send.send(clientName, TOPIC, code)
            send.disconnect(clientName)

            if code == '52':

                val = 1
                memory.insertValues('air_con_DS', {'external_val': Interior_Value, 'internal_val': Exterior_Value,'user_id':int(userid) , 'val':val})
                Devices["air conditioner"] = '1'
            if code == '53':

                val = 0
                memory.insertValues('air_con_DS', {'external_val': Interior_Value, 'internal_val': Exterior_Value,'user_id':int(userid) , 'val':val})
                Devices["air conditioner"] = '0'

            Mou.speak(EAR.intent, EAR.tense)
            return jsonify({'message': Mou.respone}), 200


    except (RuntimeError, TypeError, NameError, KeyError):
        pass

    ###############################  Curtains  ######################################
    try:
        if EAR.information['Appliance'] == 'curtains':
            code = curtains[EAR.information['State']]
            print(code)
            #print(Devices["airConditioner"])

            if code == '29' and Devices["curtains"] == '1':
                return jsonify({'message': "it's already on "}), 207

            if code == '30' and Devices["curtains"] == '0':
                return jsonify({'message': "it's already off "}), 207

            send.Conect(clientName)
            send.send(clientName, TOPIC, code)
            send.disconnect(clientName)

            if code == '29':
                Devices["curtains"] = '1'
            if code == '30':
                Devices["curtains"] = '0'

            Mou.speak(EAR.intent, EAR.tense)
            return jsonify({'message': Mou.respone}), 200


    except (RuntimeError, TypeError, NameError, KeyError):

        pass
  ################################    Fridge    ###################################
    try:
        if EAR.information['Appliance'] == 'fridge':
            code = fridge[EAR.information['State']]
            print(code)
            #print(Devices["airConditioner"])

            if code == '27' and Devices["fridge"] == '1':
                return jsonify({'message': "it's already on "}), 207

            if code == '28' and Devices["fridge"] == '0':
                return jsonify({'message': "it's already off "}), 207

            send.Conect(clientName)
            send.send(clientName, TOPIC, code)
            send.disconnect(clientName)

            if code == '27':
                Devices["fridge"] = '1'
            if code == '28':
                Devices["fridge"] = '0'

            Mou.speak(EAR.intent, EAR.tense)
            return jsonify({'message': Mou.respone}), 200


    except (RuntimeError, TypeError, NameError, KeyError):
        pass


    try:
        if EAR.information['Appliance'] == 'elevator':
            code = '31'
            print(code)
            #print(Devices["airConditioner"])


            send.Conect(clientName)
            send.send(clientName, TOPIC, code)
            send.disconnect(clientName)

            Mou.speak(EAR.intent, EAR.tense)
            return jsonify({'message': Mou.respone}), 200


    except (RuntimeError, TypeError, NameError, KeyError):
        pass


    try:
        if EAR.information['Inquiry'] == 'weather':
            print('123')
            print(EAR.information['Location'])
            tem = get_temperature(EAR.information['Location'])
            str1 = 'the weather in '
            str2 = str(EAR.information['Location'])
            str3 = ' is: '
            str4 = ' Celsius'
            strr = str1 + str2 + str3 + str(tem) + str4
            print (strr)
            return jsonify({'message': strr }), 200


    except (RuntimeError, TypeError, NameError, KeyError):
        pass


#########################################################################

 ################################    water tap    ###################################
    try:
        if EAR.information['Appliance'] == 'water tap':
            code = waterTap[EAR.information['State']]
            print(code)
            #print(Devices["airConditioner"])

            if code == '100' and Devices["waterTap"] == '1':
                return jsonify({'message': "it's already on "}), 207

            if code == '101' and Devices["waterTap"] == '0':
                return jsonify({'message': "it's already off "}), 207

            send.Conect(clientName)
            send.send(clientName, TOPIC, code)
            send.disconnect(clientName)

            if code == '100':
                Devices["waterTap"] = '1'
            if code == '101':
                Devices["waterTap"] = '0'

            Mou.speak(EAR.intent, EAR.tense)
            return jsonify({'message': Mou.respone}), 200
    except (RuntimeError, TypeError, NameError, KeyError):
        pass

    #return jsonify({'message': "Sory some times i don't understand"}), 200



    Mou.speak(EAR.intent, EAR.tense)
    return jsonify({'message': Mou.respone}), 200




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




################################################# remote API  #######################################################

@app.route('/remote', methods=['POST'])
def remote_control():
    if not request.json or not 'code' in request.json:
        abort(400)
    channel = request.json['code']

    send = Sender()
    send.Conect(clientName)
    send.send(clientName, TOPIC, channel)
    send.disconnect(clientName)

    # Call reciever to get the current state


    return jsonify({'response': "CH.NO " + channel}), 200


# ################################################# Air conditioner  API  #######################################################

# @app.route('/conditioner', methods=['POST'])
# def air_conditioner():
#     if not request.json or not 'command' in request.json:
#         abort(400)
#     command = request.json['command']

#     send = Sender()
#     send.Conect(clientName)
#     send.send(clientName, TOPIC, command)
#     send.disconnect(clientName)

#     # Call reciever to get the current state


#     return jsonify({'response': "The command you choose is " + command}), 200


@app.route('/')
def homepage():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True,host='0.0.0.0' )
