import cv2 as cv
import numpy as np

img = cv.imread("coin.bmp", cv.IMREAD_GRAYSCALE)
cv.imshow("img", img)
H, W = img.shape[:]

output = np.zeros((H, W), img.dtype)
    #valuable 선언 및 초기화
P = np.zeros(256)
hist = np.zeros(256)
q1 = np.zeros(256)
q2 = np.zeros(256)
mu1 = np.zeros(256)
mu2 = np.zeros(256)
sigma1 = np.zeros(256)
sigma2 = np.zeros(256)
sigmamu = np.zeros(256)

    #1. Calculation of histogram
for y in range(H):
    for x in range(W):
        k = img[y, x]
        hist[k] = hist[k]+1

    #2. P[] 획득
for i in range(256):
    P[i] = hist[i] / (H * W) #명암값이 i일 확률 P[i]

    #3. Otsu Algorithm
for t in range(256):
    for i in range(t+1):
        q1[t] = q1[t] + P[i]
    for i in range(t+1, 256):
        q2[t] = q2[t] + P[i]
    for i in range(t+1):
        if q1[t] > 0:
            mu1[t] = mu1[t] + i * P[i] / q1[t]
    for i in range(t+1, 256):
        if q2[t]> 0:
            mu2[t] = mu2[t] + i * P[i] / q2[t]
    for i in range(t+1):
        if q1[t] > 0:
            sigma1[t] = sigma1[t] + (i - mu1[t])**2 * P[i] / q1[t]
    for i in range(t+1, 256):
        if q2[t] > 0:
            sigma2[t] = sigma2[t] + (i - mu2[t])**2 * P[i] / q2[t]

    #4. Sigma 획득
for t in range(256):
    sigmamu[t] = q1[t] * sigma1[t] + q2[t] * sigma2[t]

    #5. 최소로 만드는 t값 획득
minSigma = np.inf
minT = 0
for i in range(256):
    if minSigma > sigmamu[i]:
        minT = i
        minSigma = sigmamu[i]

    #6. 획득된 t값을 이용해 이진화
for i in range(H):
    for j in range(W):
        if img[i, j] > minT:
            output[i, j] = 255
        else:
            output[i, j] = 0

cv.imshow("output", output)
cv.imwrite("lap02-4.png", output)
cv.waitKey(0)
