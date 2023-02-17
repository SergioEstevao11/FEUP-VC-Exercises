#Considering ex b - 2b

import numpy as np
import cv2 as cv

path = "images/xray.png"

file_name = path.split('/')

img = cv.imread(path)
img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img_grey)

res = np.hstack((img_grey,cl1)) #stacking images side-by-side
cv.imwrite('images/xray_gray_enhancement.png',res)

cv.imshow("enhancement", res)
cv.waitKey(0)
cv.destroyAllWindows()

