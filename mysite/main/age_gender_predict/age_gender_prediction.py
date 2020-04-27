import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob
import os
from django.conf import settings

def detect_face(image_name):
    #file_path= os.path.join(settings.MEDIA_ROOT,image_name)
    img = cv2.imdecode(image_name,cv2.IMREAD_UNCHANGED)
    #Rescale image
    print('Original Dimensions : ',img.shape)
    scale_percent = 50 # percent of original size
    height = int(img.shape[0] * scale_percent / 100)
    width = int(img.shape[1] * scale_percent / 100)
    dim = (width, height)
    img = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
    #Convert to image gray
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Load HAAR XML files
    facecascade = cv2.CascadeClassifier('D:\\learning\\web\\demoAI\\mysite\\main\\age_gender_predict\\haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('D:\\learning\\web\\demoAI\\mysite\\main\\age_gender_predict\\haarcascade_eye.xml')

    faces = facecascade.detectMultiScale(img_gray, scaleFactor=1.2, minNeighbors=5)
    print('nbr of faces:',len(faces))

    for (x, y, w, h) in faces:
        print(x,y,w,h)
        face_detect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = img[y:y + h, x:x + w]
        #roi_color = img[y:y + h, x:x + w]
        #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    #cv2.imwrite("D:\\learning\\web\\demoAI\\mysite\\media\\images\\result5.jpg",img)
    return cv2.imencode('.jpg',img)[1].tostring()