#Considering ex b - 2b


import cv2 as cv
import numpy as np

path = "images/apple.jpg"

file_name = path.split('/')
img = cv.imread(path)

(B, G, R) = cv.split(img)
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

clB = clahe.apply(B)
clG = clahe.apply(G)
clR = clahe.apply(R)

mergedEnhanced = cv.merge([clB, clG, clR])

res = np.hstack((img,mergedEnhanced)) #stacking images side-by-side
cv.imwrite('images/apple_enhancement.png',res)

cv.imshow("enhancement", res)

cv.waitKey(0)
cv.destroyAllWindows()