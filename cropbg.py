import cv2
import numpy as np
import random
import os

img = cv2.imread("./bg.jpeg")

x = 0
y = 0
h = 64
w = 64

k = 0

for i in range(0,33):
    for j in range(0,22):
        k = k + 1
        x = i*18
        y = j*16
        crop_img = img[y:y+h, x:x+w]
        #imgcrop = cv2.resize(crop_img,(64,64))
        filename = 'bg' + str(k) + '.png'
        filepath = os.path.join('./negative', filename)
        cv2.imwrite(filepath, crop_img)

