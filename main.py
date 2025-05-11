import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0) #Video Object

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cTime = 0
pTime = 0

while True:
    success, img = cap.read()
    if not success:
        print("Not Success")
        break

    flipped_image = cv2.flip(img, 1)

    imgRGB = cv2.cvtColor(flipped_image, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)


    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y*h)
                print(id, cx, cy)


            mpDraw.draw_landmarks(flipped_image , handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(flipped_image, str(int(fps)), (10,70), cv2.FONT_HERSHEY_SIMPLEX, 3,
                (255,0,255), 3)

    cv2.imshow("Image", flipped_image)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break