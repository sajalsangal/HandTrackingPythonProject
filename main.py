import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0) #Video Object

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    if not success:
        print("Not Success")
        break

    flipped_image = cv2.flip(img, 1)

    imgRGB = cv2.cvtColor(flipped_image, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(flipped_image , handLms, mpHands.HAND_CONNECTIONS)


    cv2.imshow("Image", flipped_image)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break