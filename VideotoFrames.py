import cv2
import math
import matplotlib.pyplot as plt
import pandas as pd
from keras.preprocessing import image
import numpy as np

count = 0
videoFile = "TestAnger.mp4"
cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5) #frame rate
print(frameRate)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % (math.floor(frameRate/5)) == 0):
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        #crop = frame
        for (x, y, w, h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),0)
            crop_img = frame[y:y+h, x:x+w]
            #crop = crop_img
        filename ="DataSet/Test/TestAnger/TestAnger%d.jpg" % count;count+=1
        cv2.imwrite(filename, crop_img)
cap.release()
print ("Done!")

