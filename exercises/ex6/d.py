import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

path = "images/apple.jpg"
scale = 1
delta = 0
ddepth = cv.CV_16S
threshhold_slider_max = 100
title_window = "gradient image"
grad = [[]]


def on_trackbar(val):
    threshold_value = cv.getTrackbarPos(val, title_window)
    _, dst = cv.threshold(grad, threshold_value, threshhold_slider_max, cv.THRESH_BINARY )
    cv.imshow(title_window, dst)

file_name = path.split('/')

img = cv.imread(path)
img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

grad_x = cv.Sobel(img_grey, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
# Gradient-Y
# grad_y = cv.Scharr(gray,ddepth,0,1)
grad_y = cv.Sobel(img_grey, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)


abs_grad_x = cv.convertScaleAbs(grad_x)
abs_grad_y = cv.convertScaleAbs(grad_y)

grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)


cv.namedWindow(title_window)

trackbar_name = "trackbar"
cv.createTrackbar(trackbar_name, title_window , 0, threshhold_slider_max, on_trackbar)

cv.imshow(title_window, grad)
cv.waitKey(0)