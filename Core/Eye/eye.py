import sys
sys.path.append('./Core/Memory')
sys.path.append('./Core/Eye/models')
sys.path.append('./Core/Eye')
import memory as Memory
from skimage import io
import csv
import dlib
import numpy
from skimage.transform import resize
from scipy.ndimage import rotate
from skimage import img_as_ubyte


predictor_path = './Core/Eye/models/shape_predictor_5_face_landmarks.dat'
face_rec_model_path = './Core/Eye/models/dlib_face_recognition_resnet_model_v1.dat'
csv_file = './Core/Eye/users_descriptors.csv'

detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(predictor_path)
facerec = dlib.face_recognition_model_v1(face_rec_model_path)


def register_password(user_name, user_pass, user_email):
    # Check if the user is exist
    query = "SELECT user_name FROM users WHERE user_name = '" + user_name + "'"
    code, _ = Memory.selectValue(query)
    if code == 501:
        # 104: this means that the user is exist.
        return 104
    # If the user is not exist
    code,ID = Memory.insertValues('users', {'user_name': user_name, 'user_pass': user_pass, 'user_email': user_email})
    if code == 201:
        return 101
    else:
        return 105


def login_password(user_name, user_pass):
    query = "SELECT user_id FROM users WHERE user_name = '" + user_name + "' AND user_pass = '" + user_pass + "'"
    code, user_id = Memory.selectValue(query)
    if code == 501:
        return code, user_name, user_id
    else:
        return code, '', ''

    
def register(userName, imgPath, user_pass):
    # Check if the user is exist
    code,uname, user_id = login(imgPath)
    if code == 201:
        # 104: this means that the user is exist.
        return 104
    # If the user is not exist
    try:
        img = io.imread(imgPath)
    except:
        # 102: this means that I can not read the picture (not Exist).
        return 102

    # img = down_scale(img)
    img = img_as_ubyte(img)
    for i in range(3):
        if i == 1:
            img = rotate(img, -90)
        elif i == 2:
            img = rotate(img, 180)

        dets = detector(img, 1)
        face_descriptor = ''
        is_face = False
        for k, d in enumerate(dets):
            is_face = True
            shape = sp(img, d)
            face_descriptor = facerec.compute_face_descriptor(img, shape)

        if is_face:
            break

    if not is_face:
        return 103, ''

    code, ID = Memory.insertValues('users', {'user_name': userName, 'user_pass': user_pass})
    with open(csv_file, 'a') as o:
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
        # img = cv2.imread(imgPath).astype(numpy.float32)
    except:
        return 202, '', ''

    #img = down_scale(img)
    img = img_as_ubyte(img)
    for i in range(3):
        if i == 1:
            img = rotate(img, -90)
        elif i == 2:
            img = rotate(img, 180)

        dets = detector(img, 1)
        face_descriptor = ''
        is_face = False
        for k, d in enumerate(dets):
            is_face = True
            shape = sp(img, d)
            face_descriptor = numpy.asarray(list(facerec.compute_face_descriptor(img, shape)), dtype='float32')

        if is_face:
            break

    if not is_face:
        return 203, '', ''

    val = 0.5
    user_id = 0

    with open('./Core/Eye/users_descriptors.csv') as csvfile:
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
        query = "SELECT user_name FROM users WHERE user_ID = '" + user_id + "'"
        code, user_name = Memory.selectValue(query)
        if code == 501:
            return 201, user_name, user_id
        else:
            # Error in the database
            return 205, user_name, user_id
    # If user is not exist
    else:
        return 204, '', ''


def down_scale(image):
    dim = image.shape[:2]
    if min(dim) > 800:
        min_size = 800
        r = (min_size / image.shape[1]) + 0.0000000001
        dim = (int(image.shape[0] * r), min_size)

        # perform the actual resizing of the image and show it
        return resize(image, dim, mode='reflect', preserve_range=False)
    else:
        return image