import numpy as np
import cv2

kernel = np.ones((5,5), np.uint8)
img = cv2.imread("resources/anglia.jpg")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7),0)
imgCanny = cv2.Canny(img, 300, 300)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow("Blur",imgBlur)
cv2.imshow("Gray",imgGray)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Dilation",imgDilation)
cv2.imshow("Erosion",imgEroded)
cv2.waitKey(0)