# add a logo to camera Video

import numpy as np
import cv2

X, Y = 10,10 # left-top of the logo

cap = cv2.VideoCapture(0)
img1 = cv2.imread('opencv_logo.png')  # background is white
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)  # background is 1
mask_inv = cv2.bitwise_not(mask)  # foreground is 1
rows, cols, channels = img1.shape
img_fg = cv2.bitwise_and(img1, img1, mask=mask_inv) # get foreground

while(1):
    ret, img2 = cap.read()
    img2 = cv2.flip(img2, 1)  # left<->right
    roi = img2[Y: Y+rows, X: X+cols] # ROI
    img_bg = cv2.bitwise_and(roi, roi, mask=mask) # get background

    dst = cv2.add(img_bg, img_fg)
    img2[Y:Y+rows, X:X+cols] = dst
    cv2.imshow('with logo', img2)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()