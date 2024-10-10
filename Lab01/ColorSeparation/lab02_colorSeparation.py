# lab02_colorSeparation into R, G, B
import cv2 as cv
import numpy as np

img = cv.imread("Mandrill.bmp", cv.IMREAD_COLOR)
cv.imshow("image", img)
H, W, C = img.shape[:] #높이 깊이 채널 개수
img2 = np.zeros((H, W, C), img.dtype) #0값을 넣음
img3 = np.zeros((H, W, C), img.dtype)
img4 = np.zeros((H, W, C), img.dtype)

h, w = img.shape[:2]


for y in range(h):
    for x in range(w):
        img2[y, x, 0] = img[y, x, 0]
        img3[y, x, 1] = img[y, x, 1]
        img4[y, x, 2] = img[y, x, 2]
cv.imwrite("lap02-1B.png", img2)
cv.imwrite("lap02-1G.png", img3)
cv.imwrite("lap02-1R.png", img4)
cv.imshow("2013755_B", img2)
cv.imshow("2013755_G", img3)
cv.imshow("2013755_R", img4)
cv.waitKey(0)

