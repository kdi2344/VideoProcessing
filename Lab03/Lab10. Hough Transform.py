import cv2 as cv
import numpy as np

img = cv.imread("edge.png", cv.IMREAD_GRAYSCALE)
H, W = img.shape[:]
output = np.zeros((H, W), img.dtype)

# 1. 행렬 생성
cm = np.zeros((H+W+1, 100), img.dtype)

# 2. 누적 행렬 구성
for y in range(H):
    for x in range(W):
        if img[y, x] == 255:
            for t in range(100):
                theta = np.pi / 100 * t
                rho = np.cos(theta)*x + np.sin(theta)*y #직접 고민하기
                r = int(rho + (H+W+1)/2) # 직접 고민하기
                cm[r , t] = cm[r, t] +1


# 3. 허프 누적 행렬의 최댓값 선정 알고리즘 작성
# theta, rho 값 획득
max = cm[0,0]
for r in range(H+W+1):
    for t in range(100):
        if max < cm[r,t]:
            max = cm[r,t]
            rho = r - (H+W+1)/2
            theta = np.pi / 100 * t

# 4. 획득한 라인 그리기

for j in range(W):
    y = rho / np.sin(theta) - j * np.cos(theta)/np.sin(theta)
    output[int(y + 0.5), j] = 255

cv.imshow("input", img)
cv.imshow("output", output)
cv.waitKey(0)
