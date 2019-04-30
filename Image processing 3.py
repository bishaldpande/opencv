import cv2
import numpy as np


img= cv2.imread('Guitar.jpg',cv2.IMREAD_COLOR)
cv2.line(img, (0,0),(150,150), (255,255,255),1 )
##CV2 uses BGR not RGB

cv2.rectangle(img,(15,15),(200,150), (0,255,0),5)
cv2.circle(img,(100,100),50,(0,0,255),-1)
##negative fills the structure with color

pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
##pts = pts.reshape((-1,1,2))
## OpenCV documentation had this code,
##which reshapes the array to a 1 x 2.

cv2.polylines(img,[pts], True,(255,0,0),1)
## True connects last two points

##For text on screen
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Text to display',(0,130), font , 1 ,(0,255,255),1 , cv2.LINE_AA)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
