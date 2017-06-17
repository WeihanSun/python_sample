# open and show image 


import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Heidelberg.jpg', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # hide tick values on X and Y axis
plt.show()
cv2.imshow('opencv', img)
cv2.waitKey(0)