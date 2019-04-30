import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Guitar.jpg', 0)
# IMREAD_COLOR OR 1 
# IMREAD_UNCHANGED OR -1 
#IMREAD_GRAYSCALE OR 0

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('grayguitar.png',img)
 
## plt is used for matplot... defined above
##plt.imshow(img, cmap='gray', interpolation='bicubic')
##plt.plot([50, 100],[100,50],'r',linewidth=5)
##plt.show()
