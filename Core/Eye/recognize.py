import PIL.Image
import PIL.ImageTk
import dlib
import numpy

predictor_path = '/root/PycharmProjects/Wattary/shape_predictor_5_face_landmarks.dat'
face_rec_model_path = '/root/PycharmProjects/Wattary/dlib_face_recognition_resnet_model_v1.dat'

detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(predictor_path)
facerec = dlib.face_recognition_model_v1(face_rec_model_path)


def getDiscriptor(img):
    dets = detector(img, 1)
    isFace = 0
    for k, d in enumerate(dets):
        isFace = 1
        shape = sp(img, d)
        face_descriptor = numpy.asarray(list(facerec.compute_face_descriptor(img, shape)), dtype='float32')
    if isFace:
        return True, face_descriptor
    return False, 103


def reco(disc):
    pass
