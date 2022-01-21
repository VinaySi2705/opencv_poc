import cv2 as cv
import numpy as np

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats',img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank',blank)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blur = cv.GaussianBlur(gray, (5,5) , cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges',canny)#canny is basically a edge detector in the image

ret, thresh = cv.threshold(gray,125,255, cv.THRESH_BINARY) #threshold will binaries the image 0 for black and 1 for white
cv.imshow('Thresh',thresh)
# What is contours?
#Contours are defined as the line joining all the points along the boundary of an image that are having the same intensity.
#Contours come handy in shape analysis, finding the size of the object of interest, and object detection.

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Blank',blank)
cv.waitKey(0)
