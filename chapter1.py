import cv2
print("Package imported")

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    cv2.imshow("Output",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break