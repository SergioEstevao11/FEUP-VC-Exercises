import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

path = "images/apple.jpg"

file_name = path.split('/')

img = cv.imread(path)
img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

scale = 1
delta = 0
ddepth = cv.CV_16S

grad_x = cv.Sobel(img_grey, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
# Gradient-Y
# grad_y = cv.Scharr(gray,ddepth,0,1)
grad_y = cv.Sobel(img_grey, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)


abs_grad_x = cv.convertScaleAbs(grad_x)
abs_grad_y = cv.convertScaleAbs(grad_y)

grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

print("combined gradient: ", grad)
