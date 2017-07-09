# transform one image to another

import numpy as np
import cv2

img1 = cv2.imread('opencv_logo.png')
img2 = cv2.imread('straw_hat.png')

w = max(img1.shape[1], img2.shape[1])
h = max(img1.shape[0], img2.shape[0])

img1 = cv2.resize(img1, (h, w))
img2 = cv2.resize(img2, (h, w))

wndName = 'transformation'
tbName = 'per'
cv2.namedWindow(wndName)
cv2.createTrackbar(tbName, wndName, 0, 100, nothing)

while(1):
    s = cv2.getTrackbarPos(tbName, wndName)
    dst = cv2.addWeighted(img1, (float)(100-s)/100, img2, (float)(s)/100, 0)
    cv2.imshow(wndName, dst)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

