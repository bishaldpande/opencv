import cv2
import numpy as np


img= cv2.imread('Guitar.jpg',cv2.IMREAD_COLOR)

##img[55,55]=[255,255,255]
##px= img[55,55]
##print(px)
##Access individual pixal and pixel modifiation


##Region of image roi
##img[100:150,100:150]= [255,255,255]
##roi=img[100:150,100:150]
##print (roi)
##gut_body = img[0:50,0:100]
##img[100:150,100:200]= gut_body

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
