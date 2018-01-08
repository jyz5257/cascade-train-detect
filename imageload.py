import cv2
import numpy as np

robot_cascade = cv2.CascadeClassifier('cascade.xml')

img = cv2.imread('m1.jpeg')
img0 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
robot = robot_cascade.detectMultiScale(img0)

print len(robot)

d = []
for i in range(0,robot.shape[0]):
    (x,y,w,h) = robot[i]
    d.append((w+h))
m = d.index(min(d))

for (w,y,w,h) in robot:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

#cv2.imwrite('detect1.jpeg', img)

cv2.namedWindow('result', cv2.WINDOW_NORMAL)

cv2.imshow('result',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
