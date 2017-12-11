###############################################################
###############################################################
################			#######################
################       WATTARY EYE	#######################
################			#######################
###############################################################
###############################################################


# Import OpenCV Library
import cv2

def faceDetect(img):	
	# Load Haarcasade File
	cascadePath = "haarcascades/haarcascade_frontalface_default.xml"
	# Declare the Cascade Classifier Object
	faceCascade = cv2.CascadeClassifier(cascadePath)
	# Detect Faces in img
	faces = faceCascade.detectMultiScale(img, 1.3, 5)
	# get the cordnates of the face
	for (x,y,w,h) in faces:
        	# draw rectangle around it
	        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		# return img with a recatngle shape around the face
		return img
	# return img if the face detection failed
	return img


cam = cv2.VideoCapture(0)
while True:
	mg, img = cam.read()
	img = face(img)
	cv2.imshow('my webcam', img)
	if cv2.waitKey(1) == 27:
		break  # esc to quit

cam.release()
cv2.destroyAllWindows()


