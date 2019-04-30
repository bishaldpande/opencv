import numpy as np
import cv2

img_bgr = cv2.imread('image1.jpg')
img_gray= cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread('image2.jpg',0)
w,h = template.shape[::-1]

res= cv2.matchTemplate(img_gray,template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc= np.where(res>= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr, pt , (pt[0]+w,pt[1]+h), (255,0,0),1)

cv2.imshow('detected', img_bgr)

cv2.waitKey(0)

cv2.destroyAllWindows()

