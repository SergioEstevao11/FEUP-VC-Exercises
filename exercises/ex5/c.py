#Considering ex b - 2b


import cv2 as cv
import numpy as np

path = "images/lowContrast_05.jpg"

file_name = path.split('/')
img = cv.imread(path)


clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

#WITH RGB
# (B, G, R) = cv.split(img)
# clB = clahe.apply(B)
# clG = clahe.apply(G)
# clR = clahe.apply(R)
# mergedEnhanced = cv.merge([clB, clG, clR])

#WITH HSV
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
(H, S, V) = cv.split(hsv_img)
clV = clahe.apply(V)
mergedEnhanced = cv.merge([H, S, clV])
mergedEnhanced = cv.cvtColor(mergedEnhanced, cv.COLOR_HSV2BGR)

res = np.hstack((img,mergedEnhanced)) #stacking images side-by-side
cv.imwrite('images/apple_enhancement.png',res)

cv.imshow("enhancement", res)

cv.waitKey(0)
cv.destroyAllWindows()