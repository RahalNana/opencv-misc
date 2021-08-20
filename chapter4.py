import cv2
import numpy as np

img = np.zeros((512, 512, 3), dtype=np.uint8)

cv2.line(img, (100, 100), (300, 300), (0, 255, 0), 3)
cv2.rectangle(img, (150, 100), (300, 350), (0, 0, 255), 2)
cv2.circle(img, (250, 250), 50, (255, 255, 0), 5)

cv2.putText(img, "OPENCV TEST", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)

cv2.imshow("Image", img)

cv2.waitKey(0)
