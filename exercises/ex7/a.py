import numpy as np
import cv2 as cv

img = cv.imread('../images/FEUP_01.jpg', cv.IMREAD_GRAYSCALE)
edges = cv.Canny(img,100,200)

cv.imshow("gauss_blur", edges)
cv.waitKey(0)
cv.destroyAllWindows()