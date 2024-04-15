import cv2
import os
import time
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)
    
if cap.isOpened():
    ret, frame = cap.read()
    print(ret)
    print(frame)
else:
    ret = False

img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

directory = r"E:/Winter semester 2023-24/ISM LAB/Honeypot project/"
os.chdir(directory)
print(os.listdir(directory)) 
filename = 'Intruder.jpg'
cv2.imwrite(filename, img1) 


cap.release()