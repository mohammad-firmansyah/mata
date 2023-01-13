import cv2
import numpy as np

lower = np.array([15,70,120])
upper = np.array([20,190,255])

video = cv2.VideoCapture(0)

while True:
    success , img = video.read()
    image = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image,lower,upper)

    countours, hir = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    print(countours)
    ret,frame = video.read()
    width = int(video.get(3))
    mid = int(video.get(3))/2
    height = int(video.get(4))
    img = cv2.line(frame,(300,0),(300,height),(255,0,0),2)
    if len(countours) != 0 :
        for c in countours:
            if cv2.contourArea(c):
                x,y,w,h = cv2.boundingRect(c)
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.imshow("mask",mask)
    cv2.imshow("webcam",img)

    cv2.waitKey(1)