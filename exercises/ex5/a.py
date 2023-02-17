import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

path = "images/xray.png"

file_name = path.split('/')

img = cv.imread(path)
img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


plt.hist(img_grey.ravel(),256,[0,256])
plt.savefig("images/xray_hist.png")
