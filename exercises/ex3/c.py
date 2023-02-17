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

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    thresh = 128
    im_bw = cv.threshold(gray, thresh, 255, cv.THRESH_BINARY)[1]

    cv.imshow("frame_binary", im_bw)
    
    
    if cv.waitKey(1) == ord('q'):
        break
    

cap.release()
cv.destroyAllWindows()