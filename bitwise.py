import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
#rectangle(img, pt1, pt2, color, thickness=None, shift=None, /)
circle = cv.circle(blank.copy(), (200,200), 200, 255 ,-1)
#circle(img, center, radius, color, thickness=None, lineType=None, shift=None, /)
cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)

#bitwise AND --> intersecting region
#bitwise_and(src1, src2. dst=None,mask=None,/)
#this basically shows the intersection of shapes of two images
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('Bitiwise AND',bitwise_and)

# bitwise OR --> non intersecting and intersecting region
#this basically returns the both images together
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise_OR',bitwise_or)

#bitwise XOR --> non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR',bitwise_xor)

#bitiwse NOT
#bitiwise_not(src, dst=None, mask=None,/)

bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Rectangle NOT',bitwise_not)

bitwise_not = cv.bitwise_not(circle)
cv.imshow('Circle NOT',bitwise_not)

cv.waitKey(0)
