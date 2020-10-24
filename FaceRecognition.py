import cv2
from cv2 import data

face_cascade = cv2.CascadeClassifier(data.haarcascades+'/haarcascade_frontalface_default.xml')
def faceRecognition(image, scaleFactor=None, minNeighbors=None):
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayImage, scaleFactor=scaleFactor, minNeighbors=minNeighbors)

    for (x, y, h, w) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return image
