import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')

ret,threshold = cv2.threshold(img, 12,255, cv2.THRESH_BINARY)

gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret2,threshold2 = cv2.threshold(gray, 12,255, cv2.THRESH_BINARY)
gaus= cv2.adaptiveThreshold(gray, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
ret3,otsu = cv2.threshold(gray, 200 ,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('original', img )
cv2.imshow('Threshold', threshold )
cv2.imshow('Threshold2', threshold2 )
cv2.imshow('Threshold3', gaus )
cv2.imshow('Thresh4', otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()
