#different functions of opencv on image

import cv2 as cv

img = cv.imread('photos/group 1.jpg')
cv.imshow('Cat',img)

#converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Blur an image
blur = cv.GaussianBlur(img,(9,9), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Edge Cascade basically edge of the images present in the pictures
cany = cv.Canny(img,125, 175)
cv.imshow('Canny',cany)

#Dilating the image
dilated = cv.dilate(cany, (7,7), iterations=1) #iterations define the width of the edge present in cany
cv.imshow('Dilated',dilated)

#Eroding
eroded = cv.erode(dilated, (7,7) ,iterations=1)#it will reverse the dilate to canny again
cv.imshow('Eroded',eroded)                     #if the magnitude used is same

#Resize
resized = cv.resize(img,(200,200),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

#Cropping
cropped = img[50:200,200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)
