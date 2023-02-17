import cv2

path = "images/apple.jpg"

file_name = path.split('/')

img = cv2.imread(path)

cv2.namedWindow(file_name[-1])

black_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

target_file = "images/apple_grey.bmp"

cv2.imwrite(target_file, img)

cv2.imshow(file_name[-1], img)

cv2.imshow('image', black_image)

cv2.waitKey(0)
cv2.destroyAllWindows()