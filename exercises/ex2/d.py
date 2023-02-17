import random
import cv2

def add_noise(img):

	row , col = img.shape
	number_of_pixels = row*col // 20
	for i in range(number_of_pixels):
		
		y_coord=random.randint(0, row - 1)
		
		x_coord=random.randint(0, col - 1)
		
		img[y_coord][x_coord] = 255
		
	number_of_pixels = row*col // 20
	for i in range(number_of_pixels):
		
		y_coord=random.randint(0, row - 1)
		
		x_coord=random.randint(0, col - 1)
		
		img[y_coord][x_coord] = 0
		
	return img

path = "images/apple.jpg"

file_name = path.split('/')

img = cv2.imread(path)

black_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

noise_img = add_noise(black_image)

cv2.imshow('image', noise_img)

cv2.imwrite('images/apple_noise.jpg', noise_img)


cv2.waitKey(0)
cv2.destroyAllWindows()