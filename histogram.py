import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats',img)

blank = np.zeros(img.shape[:2],dtype='uint8')

circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)


#Grayscale histogram
def grayscale_histogram():

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', gray)

    mask = cv.bitwise_and(gray, gray, mask=circle)
    cv.imshow('Mask',mask)

    #calcHist(images, channels, mask, histSize, ranges, hist=None,accumulate=None,/)
    gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

    plt.figure()
    plt.title('Grayscale Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')
    plt.plot(gray_hist)
    plt.xlim([0,256])
    plt.show()

#color histogram
def BGR_histogram():

    plt.figure()
    plt.title('Colour Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')

    mask = cv.bitwise_and(img, img, mask=circle)
    cv.imshow('Mask', mask)
    colors = ('b', 'g', 'r')
    for i,col in enumerate(colors):
        hist = cv.calcHist([img], [i], circle, [256], [0,256]) #circle is a mask
        plt.plot(hist, color=col)
        plt.xlim([0,256])
    plt.show()

BGR_histogram()
cv.waitKey(0)
