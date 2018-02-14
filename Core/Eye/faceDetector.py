import dlib
from skimage import io
from PIL import Image


def detectFaces(imgPath):
    # path for the CNN model.
    cnnFaceDetectorPath = './models/mmod_human_face_detector.dat'
    cnnFaceDetector = dlib.cnn_face_detection_model_v1(cnnFaceDetectorPath)

    # Read the Image as Numpy Array.
    img = io.imread(imgPath)
    # Read the image as Image object.
    image = Image.open(imgPath)
    # Detect Faces in the image
    detector = cnnFaceDetector(img)
    for i, d in enumerate(detector):
        coordinates = (d.rect.left(), d.rect.top(), d.rect.right(), d.rect.bottom())
        im = image.crop(coordinates)
        im.save('imgs/{}.jpg'.format(i))


def getTheClosestFace(imgs):
    pass

