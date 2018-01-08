import cv2
import urllib
import numpy as np

stream = urllib.urlopen('http://192.168.10.203/video/mjpg.cgi?dummy=param.mjpg')
bytes = bytes()

robot_cascade = cv2.CascadeClassifier('mrobot.xml')
k = 1

while True:
    bytes += stream.read(1024)
    a = bytes.find(b'\xff\xd8')
    b = bytes.find(b'\xff\xd9')
    if a != -1 and b != -1:
        jpg = bytes[a:b+2]
        bytes = bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
        img0 = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
        robot = robot_cascade.detectMultiScale(img0)
        d = []
        #print robot
        #print len(robot)
        if len(robot)>0:
            for i in range(0,robot.shape[0]):
                (x,y,w,h) = robot[i]
                d.append((w+h))
            m = d.index(min(d))
            (x,y,w,h) = robot[m]
            
            i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            cv2.rectangle(i,(x,y),(x+w,y+h),(255,255,0),1)

        cv2.imshow('i', i)
        
        if cv2.waitKey(1) == 27:
            #out.release
            exit(0)
            cv2.destroyAllWindows()

        if cv2.waitKey(0) == ord('1'):
            filename = '.errors/error' + str(k) + '.jpeg'
            cv2.imwrite(filename, i)
            k = k+1

        if cv2.waitKey(0) == ord('2'):
            print k
