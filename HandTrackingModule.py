import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode = False, maxHands = 2, model_complexity = 1, detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.model_complexity = model_complexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.model_complexity, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils


    def findHands(self, flipped_image, draw = True):
        imgRGB = cv2.cvtColor(flipped_image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(flipped_image, handLms, self.mpHands.HAND_CONNECTIONS)
        return flipped_image

    def findPosition(self, flipped_image, handNo = 0, draw = True):
        lmList = []
        for id, lm in enumerate(handLms.landmark):
            # print(id,lm)
            h, w, c = flipped_image.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            print(id, cx, cy)

        return LmList

def main():
    cap = cv2.VideoCapture(0)  # Video Object
    cTime = 0
    pTime = 0
    detector = handDetector()
    while True:
        success, img = cap.read()
        if not success:
            print("Not Success")
            break

        flipped_image = cv2.flip(img, 1)
        final_image = detector.findHands(flipped_image)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(final_image, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3,
                    (255, 0, 255), 3)

        cv2.imshow("Image", final_image)
        cv2.waitKey(1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()