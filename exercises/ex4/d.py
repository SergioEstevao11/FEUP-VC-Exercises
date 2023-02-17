import os
import numpy as np
from matplotlib import pyplot as plt
import cv2
from scipy import ndimage
# Read image
img = cv2.imread(os.path.join('images/apple_noise.jpg'))
# Convert to grayscale if needed
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Smooth us ing OpenCV GaussianBlur()
gaussianBlurred = cv2.GaussianBlur(img, (3 ,3 ), 0 )
# Smooth using convolution operation coded below

kernel3x3 = (1/16 )* np.array([[1 , 2 , 1 ],[2 , 4 , 2 ],[1 , 2 , 1 ]])

#By removing the 1/16, the image is more blured and distorted, since the attenuation is higher
#kernel3x3 = np.array([[1 , 2 , 1 ],[2 , 4 , 2 ],[1 , 2 , 1 ]])

print(kernel3x3 )
myConvolutionResult = ndimage.convolve(img, kernel3x3 )
# Show results
cv2.imshow("Original" , img)
cv2.imshow("OpenCV Gaussian Blur" , gaussianBlurred)
cv2.imshow("My 3x3 convolution w/Gaussian mask" , myConvolutionResult)
cv2.waitKey(0)
cv2.destroyAllWindows()