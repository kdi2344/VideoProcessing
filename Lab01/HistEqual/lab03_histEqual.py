import cv2 as cv
import numpy as np

img = cv.imread("citrus.bmp", cv.IMREAD_GRAYSCALE)
cv.imshow("img", img)
H, W = img.shape[:]

output = np.zeros((H, W), img.dtype)
#valuable 선언 및 초기화
hist = np.zeros((256), int)
sum_of_hist = np.zeros((256), int)

#1. Calculation of histogram
for y in range(H):
    for x in range(W):
        k = img[y, x]
        hist[k] = hist[k]+1

sum=0
#2. Cumulative Histogram
for i in range(256):
    sum = sum + hist[i]
    sum_of_hist[i] = sum
    #작성


#3. Transform the input image to output image
area = H * W
Dm = 255
for i in range(H):
    for j in range(W):
       k = img[i,j]
       output[i,j] = (Dm / area) * sum_of_hist[k]

cv.imshow("output", output)
cv.imwrite("lap02-3.png", output)
cv.waitKey(0)
