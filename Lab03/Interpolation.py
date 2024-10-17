import cv2 as cv
import numpy as np
import math

src = cv.imread("Mandrill.bmp", cv.IMREAD_COLOR)
H, W, C = src.shape[:]
cv.imshow("Origin", src)

ratioX = 5
ratioY = 3

dst = np.zeros((H*ratioY, W*ratioX, C), src.dtype)

cols = H
rows = W

for yd in range (ratioY * cols):
    for xd in range (ratioX * rows):
        xo = xd / ratioX #소수
        yo = yd / ratioY #소수

        xleft = math.floor(xo)
        xright = math.ceil(xo)
        yup = math.floor(yo)
        ydown = math.ceil(yo)
            #(yup, xleft) (yup, xright)
            #(ydown, xleft) (xup, xright)

        a = xo - xleft #알파
        b = yo - yup #베타

        if (xright > 255): xright = 255
        if (ydown > 255): ydown = 255
        dst[yd, xd] = (1-a) * (1-b) * src[yup, xleft] + a * (1-b) * src[yup, xright] + (1-a) * b * src[ydown, xleft] + a * b * src[ydown, xleft]

cv.imshow("Interpolation", dst)
cv.imwrite("./Interpolation.bmp", dst)
cv.waitKey(0)