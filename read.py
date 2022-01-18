import cv2 as cv

#reading images
img = cv.imread('photos/cat_large.jpg')
cv.imshow('Cat', img)
cv.waitKey(0)
