import cv2
import glob
import os

file = open('negative.txt','w')

for im_path in glob.glob(os.path.join('neg', "*")):
    l = len(im_path)
    filename = im_path[0:3] + '/' + im_path[4:l]
    file.write(filename)
    file.write('\n')
file.close()
