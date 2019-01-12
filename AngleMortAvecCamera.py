import cv2
import numpy as np
import sys
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import RPi.GPIO as GPIO

redLed=21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(redLed,GPIO.OUT)

camera = PiCamera()
camera.resolution=(320,240)
camera.framerate = 30
rawCapture = PiRGBArray(camera,size=(320,240))
display_window=cv2.namedWindow("video")
car_cascade = cv2.CascadeClassifier('cars.xml')
GPIO.output(redLed,GPIO.LOW)
ledOn = False
time.sleep(1)
#Tant que le Camera capture
for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True) :

    image = frame.array
    #convertir la video en grey
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #detection voiture
    cars = car_cascade.detectMultiScale(gray, 1.1, 3)

    #Dessiner le rectangle sur la voiture et Allumer la LED 
    for (x,y,w,h) in cars:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)      
        if not ledOn :
		GPIO.output(redLed,GPIO.HIGH)
		ledOn = True
		time.sleep(2)
    GPIO.output(redLed,GPIO.LOW)
    ledOn = False	
    #Afficher la frame
    cv2.imshow('video', image)
    rawCapture.truncate(0)
    #Q pour exiter
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
#Fermer la camera
camera.close()
#Fermer les Frames
cv2.destroyAllWindows()
