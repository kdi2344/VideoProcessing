import cv2 as cv
import numpy as np

#Dilation
def Dilation(src,size):
    H,W = src.shape[:]
    dst = np.zeros((H, W), src.dtype)

    for i in range(H):
        for j in range(W):
            max = -1
            for mi in range(-size, size+1):
                for mj in range(-size, size+1):
                    if (0 < i + mi < H) and (0 < j + mj < W):
                        k = src[i + mi, j + mj]
                        if (k > max):
                            max = k

            dst[i, j] = max
    return dst

#Erosion
def Erosion(src,size):
    H,W = src.shape[:]
    dst = np.zeros((H, W), src.dtype)

    for i in range(H):
        for j in range(W):
            min = 999
            for mi in range(-size, size+1):
                for mj in range(-size, size+1):
                    if (0 < i + mi < H) and (0 < j + mj < W):
                        k = src[i + mi, j + mj]
                        if (k < min):
                            min = k

            dst[i, j] = min
    return dst

#Opening
def Opening(src, size):
    dst = Erosion(src,size)
    dst = Dilation(dst,size)
    return dst

#Otsu
def binary(dst):
    output = np.zeros((H, W), dst.dtype)
    P = np.zeros(256)
    hist = np.zeros(256)
    q1 = np.zeros(256)
    q2 = np.zeros(256)
    mu1 = np.zeros(256)
    mu2 = np.zeros(256)
    sigma1 = np.zeros(256)
    sigma2 = np.zeros(256)
    sigmamu = np.zeros(256)

    for y in range(H):
        for x in range(W):
            k = dst[y, x]
            hist[k] = hist[k] + 1

    for i in range(256):
        P[i] = hist[i] / (H * W)  # 명암값이 i일 확률 P[i]

    for t in range(256):
        for i in range(t + 1):
            q1[t] = q1[t] + P[i]
        for i in range(t + 1, 256):
            q2[t] = q2[t] + P[i]
        for i in range(t + 1):
            if q1[t] > 0:
                mu1[t] = mu1[t] + i * P[i] / q1[t]
        for i in range(t + 1, 256):
            if q2[t] > 0:
                mu2[t] = mu2[t] + i * P[i] / q2[t]
        for i in range(t + 1):
            if q1[t] > 0:
                sigma1[t] = sigma1[t] + (i - mu1[t]) ** 2 * P[i] / q1[t]
        for i in range(t + 1, 256):
            if q2[t] > 0:
                sigma2[t] = sigma2[t] + (i - mu2[t]) ** 2 * P[i] / q2[t]

    for t in range(256):
        sigmamu[t] = q1[t] * sigma1[t] + q2[t] * sigma2[t]

    minSigma = np.inf
    minT = 0
    for i in range(256):
        if minSigma > sigmamu[i]:
            minT = i
            minSigma = sigmamu[i]

    for i in range(H):
        for j in range(W):
            if dst[i, j] > minT:
                output[i, j] = 255
            else:
                output[i, j] = 0
    return output

src = cv.imread("rice.bmp",cv.IMREAD_GRAYSCALE) #Read the file
opened = Opening(src, 7)

H,W = src.shape[:]
dst = np.zeros((H, W), src.dtype)

for i in range(H):
    for j in range(W):
        diff = np.int32(src[i, j]) - np.int32(opened[i, j])
        if  diff < 0:
            diff = 0
        dst[i, j] = diff

output = binary(dst)
cv.imshow("TopHat", output)
cv.imwrite("./TopHat.bmp", output)
cv.waitKey(0)