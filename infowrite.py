import cv2
import glob
import os

file = open('pos.lst','w')

for im_path in glob.glob(os.path.join('pos', "*")):
    filename = im_path[10:] +' '+'1'+' '+'0'+' '+'0'+' '+'64'+' '+'64'
    file.write(filename)
    file.write('\n')
file.close()
