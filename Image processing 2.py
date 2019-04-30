import cv2
import numpy as np
## Rember to release after taking control


cap= cv2.VideoCapture(0)
##0 for first webcam, 1 for second,...

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out =cv2.VideoWriter('Output.avi',fourcc, 20.0, (640,480))

while True:
    ret, frame= cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ## cvt-> convert
    out.write(frame)
    cv2.imshow('frame', frame)
    cv2.imshow('frame1', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
