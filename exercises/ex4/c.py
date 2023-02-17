import numpy as np
import cv2 as cv

path = "images/apple_noise.jpg"

file_name = path.split('/')

img = cv.imread(path)

blur = cv.bilateralFilter(img,9,75,75)

cv.imshow("bilateral_blur", blur)
cv.waitKey(0)
cv.destroyAllWindows()