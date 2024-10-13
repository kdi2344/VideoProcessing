import cv2 as cv
import numpy as np

src = cv.imread("pepper_noise.bmp", cv.IMREAD_GRAYSCALE)
H,W = src.shape[:]
dst = np.zeros((H,W), src.dtype)
array = np.zeros(9, src.dtype)

for i in range(H):
    for j in range(W):
        num=0
        for mi in range(-1,2):
            for mj in range(-1,2):
                if(0 < i + mi < H) and (0 < j + mj < W):
                    array[num]=src[i+mi,j+mj]
                    num +=1

        for si in range(num-1):
            for sj in range(num-1-si):
                if array[sj] > array[sj+1]:
                    array[sj], array[sj+1] = array[sj+1], array[sj]
        dst[i,j] = array[int(num/2)]

cv.imwrite("./median_filtering.bmp", dst)
cv.imshow("median_filtering", dst)
cv.waitKey(0)