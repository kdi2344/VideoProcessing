# lab02_inverse
import cv2 as cv
import numpy as np

img = cv.imread("rice.bmp", cv.IMREAD_GRAYSCALE)
H, W= img.shape[:]
img_inverse = np.zeros((H, W), img.dtype)
for y in range(H):
    for x in range(W):
        img_inverse[y,x]= 255 - img[y, x]

cv.imwrite("inverse.png",img_inverse)

cv.imshow("image",img)
cv.imshow("image_inverse", img_inverse)
cv.waitKey(0)
