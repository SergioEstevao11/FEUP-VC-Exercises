import numpy as np
import cv2 as cv

t=100
s=200


img = cv.imread('../images/FEUP_01.jpg')
img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny_edges = cv.Canny(img_grey,t,s)

blur = cv.GaussianBlur(img_grey,(5,5),0)

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

res = np.hstack((canny_edges,grad)) #stacking images side-by-side


cv.imshow("canny vs sober", res)
cv.waitKey(0)
cv.destroyAllWindows()


