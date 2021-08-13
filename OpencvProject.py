# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 00:06:23 2021

@author: hp
"""

# py file in main and xml file in source + store video in source folder


# Importing Libraries 
import cv2 
import time
from random import randrange
#import imutils

# URL of camera for capturing video
#url = "http://...................................//video"  #url of camera
cap = cv2.VideoCapture(0)  # For using PC camera

# Capturing Video
#cap = cv2.VideoCapture(url)  

# Using Haarcascade classifier for detecting eye and face
detect_eye = cv2.CascadeClassifier('source/haarcascade_eye.xml')
detect_face = cv2.CascadeClassifier('source/haarcascade_frontalface_default.xml')

# Width and Height for recorder screen
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# Storing Video
#writer=cv2.VideoWriter('video//cam_recording.avi',cv2.VideoWriter_fourcc(*'DIVX'),20,(width,height))
writer=cv2.VideoWriter('source/myvideo.mp4',cv2.VideoWriter_fourcc(*'DIVX'),20,(width,height))
# Running of while loop and get exit after pressing 'Esc' key
while(True):

    # Reading of frames    
    ret, frame = cap.read()
    if frame is not None:
        #frame = imutils.resize(frame, width=850)
        # Converting to gray scale to make it easy for detection
        gray = cv2.cvtColor(frame, 0)
        # To count no of faces i.e Persons
        person_count = 1
        detect = detect_face.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
        if(len(detect) > 0):
           # Face detecting and Making a rectangle  
           for (x,y,w,h) in detect:
             frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(256),0,0),2)  
             #Displaying Person Count
             cv2.putText(frame,f'Person {person_count}', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
             person_count += 1      
             
             # Eye detecting and making small rectangle 
             color_frame=frame[y:y+h,x:x+w]
             detections_eye = detect_eye.detectMultiScale( gray[y:y+h,x:x+w],scaleFactor=1.3,minNeighbors=5)
             for (ex,ey,ew,eh) in detections_eye :
                 cv2.rectangle(color_frame,(ex,ey),(ex+ew,ey+eh),(0,randrange(256),0),2)
        # Getting local time of PC         
        localtime = time.asctime( time.localtime(time.time()) ) 
        
        # Putting imformation like Local Time ,Detection mode and Total Person count
        cv2.putText(frame, f'Local Time : {localtime}', (40,40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 2)
        cv2.putText(frame, 'Detection Mode ON', (40,70), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0,0,255), 2)
        cv2.putText(frame, f'Total Persons : {person_count-1}', (40,100), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 2)
       
        # Storing captured video     
        writer.write(frame)
        cv2.imshow('Cam_Video',frame)

        # Press 'Esc' to stop everything        
        if cv2.waitKey(1) == 27 :
         break
     
        
cap.release()  
writer.release()
cv2.destroyAllWindows()



# OpenCV Project by ABHIJEET
