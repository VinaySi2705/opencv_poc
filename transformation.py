import cv2 as cv
import numpy as np
img = cv.imread('photos/park.jpg')
cv.imshow('Park',img)

#Translation basically shifting the image from left to right or up down
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)
# -x --> Left  (negative value of x)
# -y --> Up    (negative value of y)
# x --> Right  (positive value of x)
# y --> Down   (positive value of y)

translated = translate(img, 100, 100) #here we pass the value of x and y which defines how many pixels we want to shift the image
cv.imshow('Translated',translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)
# -ve angle for rotation of image clockwise
# +ve angle for rotation of image anti-clockwise
rotated = rotate(img, -45) #image to rotate and angle
cv.imshow('Rotated',rotated)

#Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#Flipping an image
flip = cv.flip(img,1)
#0 flipping the image vertically over the x-axis
#-1 flipping the image vertically as well as horizontallly both
#1 flipping the image horizontallly over the y-axis
cv.imshow('Flipping',flip)
cv.waitKey(0)
