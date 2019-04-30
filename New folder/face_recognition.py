import cv2
import numpy as np
import urllib.request
#import serial
faceDetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
rec = cv2.face.LBPHFaceRecognizer_create()

rec.read("trainer\\trainer.yml")



url = 'http://192.168.1.88:8088/html/cam_pic.php?time=1533210339086&pDelay=40000'
id = 0
font = cv2.FONT_HERSHEY_SIMPLEX

#ser1= serial.Serial('COM7', 9600)

while True:
    id = 0;
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)

    
    
   # ret, img = image.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.2, 5)
    
    for x,y,w,h in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
        id, conf = rec.predict(gray[y:y+h, x:x+w])
        c = 100- conf
        
        print('id = {} conf = {}'.format(id ,c))
        
                 
        if id == 1: name = "Bishal"
        
        else:
            name="Intruder"
        if conf > 90:
            name = 'Intruder'
            
        
       
        tag = name+ ' (confidence = '+ str(conf) +")"  
        cv2.putText(img, tag,(x,y+h),font,0.8,(255,0,0), 2)
            
##        if id in range(1,8) :
##           ser1.write('s'.encode())
##        else:
##            ser1.write('q',encode())
        
        

    cv2.imshow("Face_Detection_App", img)
    if cv2.waitKey(1)==ord("q"):
        break
# cam.release()
cv2.destroyAllWindows()
