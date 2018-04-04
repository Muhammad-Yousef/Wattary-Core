#
# Eye API Version 1.0
#
# This module plays as a mid-way communicator between the Eye and users
# To easily detect and add a new user to database and check if this face exist or not
#
# Written By: Ahmed Abdeldaim
#
# To use this module well:
# please read the following lines.
#
# To load this module in your script, use:
# >>> from Eye import eye
# or
# >>> import Eye.eye
# or
# >>> import Eye.eye as anyName
##############################################################################################
#
# To add a user to the database
# use function register(params)
# - this function takes 2 parameters:
#   1- User name. Ex: Sayed Mahmoud
#   2- a full url of his picture. Ex: https://www.pictures.com/img_002314562.jpg
#
# - and returning 1 value:
#   1- code. Ex: 101.
#
#   code meaning:
#   101: this means the operation succeeded.
#   102: this means that I can not read the picture (not Exist).
#   103: this means that I can not find any faces in the picture (retake a picture)
#   104: this means that the user is exist.
#   105: this means a memory (database) error.
#
# Ex:
#   code = register('Ahmed Abdeldaim', 'https://www.pictures.com/img_002314562.jpg')
#
#
# To recognize a face from a picture
# use function login(params)
# - this function takes 1 parameters:
#   1- a full url of his picture. Ex: https://www.pictures.com/img_002314562.jpg
#
# - and returning 2 value:
#   1- code. Ex: 201.
#   2- userID (if exist else null)
#
#   code meaning:
#   201: this means that the user is exist.
#   202: this means that I can not read the picture (not Exist).
#   203: this means that I can not find any faces in the picture (retake a picture)
#   204: this means that the user is exist.
#   205: this means a memory (database) error.
#   206: this means that I can not recognize this person.
#
# Ex:
#   code, userID = login('https://www.pictures.com/img_002314562.jpg')
#
# Import the database API from the parent directory.
from Core.Memory.memory import *
#from faceRecognitionDemo
from recognize import *
from skimage import io
import numpy


def register(userName, imgPath):
    try:
        img = io.imread(imgPath)
    except:
        return 102
    code, disc = recognize.getDiscriptor(img)
    if code == 103:
        return code
    code, u = checkUser(disc)
    if code:
        return code
    face_descriptor = ', '.join(str(i) for i in list(disc))
    code = Memory.insertValues('users', {'user_name': userName,
                                         'user_face': imgPath,
                                         'face_descriptor': '{' + face_descriptor + '}'})
    if code == 201:
        return 101
    else:
        return 105


def login(imgPath):
    try:
        img = io.imread(imgPath)
    except:
        return 202
    code, disc = recognize.getDiscriptor(img)
    if code == 203:
        return code
    code, u = checkUser(disc)
    if code == 104:
        return 201, u
    else:
        return 206, ''


def checkUser(discriptor):
    code, data = Memory.getValuesAll('users', ['face_descriptor'])
    if code != 401:
        return 105
    userName = 'Unknown'
    val = 0.5
    for row in data:
        savedDist = numpy.asarray(row[0], dtype='float32')
        dist = numpy.linalg.norm(discriptor - savedDist)
        if dist < val:
            userName = 'known'

    if userName != 'Unknown':
        # IF user is Exist
        return 104, userName
    else:
        return 0, userName
