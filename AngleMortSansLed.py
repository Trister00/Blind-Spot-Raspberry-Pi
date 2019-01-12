import cv2
import numpy as np


#Lire la Video
cap = cv2.VideoCapture('test1.mp4')
#Utilise le classifier XML
car_cascade = cv2.CascadeClassifier('cars.xml')

#Tant que la Video n'a pas termine
while True:
    #Lire FRame by Frame
    ret, frame = cap.read()
    #conversion en grey
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detection de la voiture
    cars = car_cascade.detectMultiScale(gray, 1.1, 3)

    #dessiner un Rectangle sur la voiture
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)    
	
    #Afficher Le resultat
    cv2.imshow('video', frame)
    #Q pour exiter
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
#release la video
cap.release()
#Fermer les Frames
cv2.destroyAllWindows()
