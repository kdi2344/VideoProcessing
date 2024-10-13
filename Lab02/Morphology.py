from nt import scandir
from sys import deactivate_stack_trampoline

import cv2 as cv
import numpy as np

#Dilation
def Dilation(src):
    H,W = src.shape[:]
    dst = np.zeros((H, W), src.dtype)

    for i in range(H):
        for j in range(W):
            max = -1
            for mi in range(-4, 5):
                for mj in range(-4, 5):
                    if (0 < i + mi < H) and (0 < j + mj < W):
                        k = src[i + mi, j + mj]
                        if (k > max):
                            max = k

            dst[i, j] = max
    return dst

#Erosion
def Erosion(src):
    H,W = src.shape[:]
    dst = np.zeros((H, W), src.dtype)

    for i in range(H):
        for j in range(W):
            min = 999
            for mi in range(-4, 5):
                for mj in range(-4, 5):
                    if (0 < i + mi < H) and (0 < j + mj < W):
                        k = src[i + mi, j + mj]
                        if (k < min):
                            min = k

            dst[i, j] = min
    return dst

def Closing(src):
    dst = Dilation(src)
    dst = Erosion(dst)
    return dst

src = cv.imread("coin.bmp",cv.IMREAD_GRAYSCALE) #Read the file
dilated = Dilation(src)
erosioned = Erosion(src)
closed = Closing(src)

cv.imshow("Dilation", dilated)
cv.imshow("Erosion", erosioned)
cv.imshow("Close", closed)
cv.imwrite("./Dilation.bmp", dilated)
cv.imwrite("./Erosion.bmp", erosioned)
cv.imwrite("./Close.bmp", closed)
cv.waitKey(0)