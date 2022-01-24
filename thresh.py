import cv2 as cv
import numpy as np

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholding', thresh)

#threshold_inv will inverse the colors of threshold image which we get by thresh
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholding Inverse', thresh_inv)

# Adaptive Thresholding
#this will automatically consider the thresholded pixel value
#adptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C, dst=None, /)
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                  cv.THRESH_BINARY_INV, 13, 9)
cv.imshow('Adaptive Thresholding',adaptive_thresh)


cv.waitKey(0)
