import cv2

path = "images/apple.jpg"

file_name = path.split('/')

img = cv2.imread(path)

(B, G, R) = cv2.split(img)

R = R + 10

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)

cv2.waitKey(0)
cv2.destroyAllWindows()