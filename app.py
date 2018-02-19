from flask import Flask, abort
from flask import request
from flask import jsonify
from flask_cors import CORS
from Core.sender import Sender
from flask import render_template, render_template_string


app = Flask(__name__)
cors = CORS(app, resources={r"/analyze/*" : {"origins": "*"}})
cors1 = CORS(app, resources={r"/remote/*" : {"origins": "*"}})
clientName = 'user'
TOPIC = 'PI'


################################################# analyze API  #######################################################
@app.route('/analyze', methods=['POST'])
def analyze_data():
    if not request.json or not 'message' in request.json:
        abort(400)
    message = request.json['message']

    # NLP processing

    send = Sender()
    send.Conect(clientName)
    send.send(clientName , TOPIC , message)
    send.disconnect(clientName)

    # Call reciever to get the current state


    # NLG TO generate response


    # save the data in db

    return jsonify({'message': message}), 200

################################################# remote API  #######################################################

@app.route('/remote', methods=['POST'])
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






@app.route('/')
def homepage():


    return render_template('index.html')




if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)
