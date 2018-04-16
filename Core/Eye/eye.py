# Please Fix the path to use this model well
from Core.Memory import memory as Memory
from skimage import io
import csv
import dlib
import numpy

predictor_path = './models/shape_predictor_5_face_landmarks.dat'
face_rec_model_path = './models/dlib_face_recognition_resnet_model_v1.dat'

detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(predictor_path)
facerec = dlib.face_recognition_model_v1(face_rec_model_path)


def register(userName, imgPath):
    # Check if the user is exist
    code, user_id = login(imgPath)
    if code == 201:
        # 104: this means that the user is exist.
        return 104
    # If the user is not exist
    try:
        img = io.imread(imgPath)
    except:
        # 102: this means that I can not read the picture (not Exist).
        return 102

    dets = detector(img, 1)
    face_descriptor = ''
    is_face = False
    for k, d in enumerate(dets):
        is_face = True
        shape = sp(img, d)
        face_descriptor = facerec.compute_face_descriptor(img, shape)

    if not is_face:
        # 103: this means that I can not find any faces in the picture (retake a picture)
        return 103

    code, ID = Memory.insertValues('users', {'user_name': userName})
    with open('./users_descriptors.csv', 'a') as o:
        fieldnames = ['user_ID', 'descriptor']
        writer = csv.DictWriter(o, fieldnames=fieldnames)
        writer.writerow({'user_ID': ID, 'descriptor': face_descriptor})

    if code == 201:
        return 101
    else:
        return 105


def login(imgPath):
    try:
        img = io.imread(imgPath)
    except:
        return 202

    dets = detector(img, 1)
    face_descriptor = ''
    is_face = False
    for k, d in enumerate(dets):
        is_face = True
        shape = sp(img, d)
        face_descriptor = numpy.asarray(list(facerec.compute_face_descriptor(img, shape)), dtype='float32')

    if not is_face:
        return 203, ''

    val = 0.5
    user_id = 0

    with open('./users_descriptors.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            j = numpy.asarray(row['descriptor'].split('\n'), dtype='float32')
            label = row['user_ID']
            dist = numpy.linalg.norm(face_descriptor - j)
            if dist < val:
                val = dist
                user_id = label

    # If user is exist
    if user_id != 0:
        return 201, user_id
        # If user is not exist
    else:
        return 204, ''
