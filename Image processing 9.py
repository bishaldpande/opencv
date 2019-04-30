import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([150, 150,50])
    upper_red = np.array([255,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res= cv2.bitwise_and(frame, frame, mask= mask)

    kernal = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernal, iterations=1)
    dialation = cv2.dilate(mask, kernal, iterations=1)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN,kernal)
    Closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE,kernal)
    
    ##OPENING and closing to remove false positive and negative

    tphat, blackhat
    

    cv2.imshow('Frame',opening)
    cv2.imshow('Frame2',Closing)
    cv2.imshow('erosion',tophat)
    cv2.imshow('dialation',blackhat)
    
    

    k= cv2.waitKey(5) & 0xFF
    if k==27:
        break
    

cv2.destroyAllWindows()
cap.release()
