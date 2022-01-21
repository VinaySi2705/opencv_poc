import cv2 as cv

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats',img)

# Averaging
#this will define a kernel window of given size i.e.
#3*3 and blur it after taking the average value of surrounding pixels towards center of the matrix of each window
average = cv.blur(img, (3,3))
cv.imshow('Average',average)

# Gaussian blur
#it is more natural then averaging blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur',gauss)

#Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur',median)


cv.waitKey(0)
