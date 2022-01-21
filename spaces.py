import cv2 as cv
import matplotlib.pyplot as plt

#opencv read the images in BGR(blue,Green,red) color
img = cv.imread('photos/park.jpg')
cv.imshow('Park',img)

# plt.imshow(img)
# this will shows the image in RGB color
# plt.show()
#BGR to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


#BGR to HSV(Hue Saturation Value)
"""
HSV Color Scale: The HSV (which stands for Hue Saturation Value) scale provides a numerical readout of your image that corresponds to the color names contained therein.
Hue is measured in degrees from 0 to 360.
"""
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

"""
The Lab* color space allows you to quantify the color utilizing an independent color space.
This means that the values give you an independent value representing that color.
In the simplest terms, if you have the same Lab* values you will have the same color, different lab* values a different color.
he CIELAB color space also referred to as L*a*b* is a color space defined by the International Commission on Illumination (abbreviated CIE) in 1976. ...
It expresses color as three values: L* for perceptual lightness, and a* and b* for the four unique colors of human vision: red, green, blue, and yellow.
"""
#BGR to L*a*b
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV->BGR',hsv_bgr)

plt.imshow(rgb)
plt.show()


cv.waitKey(0)
