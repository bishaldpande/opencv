import cv2
import numpy as np
import urllib.request

detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
url = 'http://192.168.1.88:8088/html/cam_pic.php?time=1533210339086&pDelay=40000'

Id=input('enter your id')
sampleNum=0
while(True):
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
   # ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
        #incrementing sample number 
        sampleNum=sampleNum+1
        #saving the captured face in the dataset folder
        cv2.imwrite("dataset/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

    cv2.imshow('frame',img)
    #wait for 100 miliseconds 
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    # break if the sample number is morethan 50
    elif sampleNum>50:
        break
#cam.release()
cv2.destroyAllWindows()
