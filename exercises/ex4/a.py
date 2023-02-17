import numpy as np
import cv2 as cv

path = "images/apple_noise.jpg"

file_name = path.split('/')

img = cv.imread(path)

blur = cv.GaussianBlur(img,(5,5),0)

cv.imshow("gauss_blur", blur)
cv.waitKey(0)
cv.destroyAllWindows()