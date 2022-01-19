import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow('Blank',blank)

# 1. Paint the image a certain colour
blank[200:300,300:400] = 0,255,0
# cv.imshow('Green',blank)

#2. Draw a Rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
cv.imshow('Rectangle',blank)
cv.waitKey(0)
