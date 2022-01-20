import cv2 as cv

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges',canny)

# What is contours?
#Contours are defined as the line joining all the points along the boundary of an image that are having the same intensity.
#Contours come handy in shape analysis, finding the size of the object of interest, and object detection.

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.waitKey(0)
