import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

# 1. Paint the image a certain colour
blank[200:300,300:400] = 0,255,0
cv.imshow('Green',blank)

#2. Draw a Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle',blank)

#3. Draw circle
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle',blank)

#4. Draw a line
cv.line(blank,(100,250),(300,300),  (255,255,255),thickness=3)# after blank quadrant is given of the line first quadrant from where lne starts and second quadrant where it ends
cv.imshow('Line',blank)

#5. Write text on image
cat = cv.imread('photos/cat.jpg')
cv.putText(cat,'Hello, my name is Vinay..', (100,100), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text',cat)
cv.waitKey(0)
