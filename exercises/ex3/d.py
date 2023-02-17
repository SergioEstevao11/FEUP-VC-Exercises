import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    hsv_img = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    thresh = 128
    im_bw, thresh = cv.threshold(hsv_img, thresh, 255, cv.THRESH_BINARY)

    
    cv.imshow('bitwise', frame & thresh)

    
    
    if cv.waitKey(1) == ord('q'):
        break
    

cap.release()
cv.destroyAllWindows()