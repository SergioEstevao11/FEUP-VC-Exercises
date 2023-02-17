import numpy as np
import cv2 as cv

path = "images/apple_noise.jpg"

file_name = path.split('/')

img = cv.imread(path)

blur = cv.medianBlur(img,5)

cv.imshow("median_blur", blur)
cv.waitKey(0)
cv.destroyAllWindows()