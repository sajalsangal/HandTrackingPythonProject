import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0) #Video Object


while True:
    success, img = cap.read()
    if not success:
        print("Not Success")
        break

    flipped_image = cv2.flip(img, 1)


    cv2.imshow("Image", flipped_image)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break