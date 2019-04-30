import cv2
import numpy as np

im1= cv2.imread('image1.png')
im2= cv2.imread('im3.png')

##add = im1 + im2

##add= cv2.add(im1,im2)
##Add individual pixel

##add_weighted = cv2.addWeighted(im1,0.6, im2, 0.4,0)

rows,cols,channels = im2.shape
roi=im1[0:rows,0:cols]

im2gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(im2gray,220,255,cv2.THRESH_BINARY_INV)
##

mask_inv= cv2.bitwise_not(mask)

im1_bg = cv2.bitwise_and(roi,roi,mask= mask_inv)
im2_fg = cv2.bitwise_and(im2,im2, mask=mask)
## make BG or FG black(0)s


dst=cv2.add(im1_bg,  im2_fg)
im1[0:rows,0:cols]= dst

cv2.imshow('added', im1)
cv2.imshow('added1', mask)
cv2.imshow('added2', mask_inv)
cv2.imshow('added3', dst)
cv2.imshow('added4', im1_bg)
cv2.imshow('added5', im2_fg)



cv2.waitKey(0)
cv2.destroyAllWindows()


