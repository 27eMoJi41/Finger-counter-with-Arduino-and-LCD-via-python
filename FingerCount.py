import cv2
import time
import HandDetection as hd

class FingerCount:
    def counter(self,img):
        self.detector = hd.handDetector(detectionCon=0.75)
        self.lmList = self.detector.findPosition(img, draw=False)
        self.tipIds = [4, 8, 12, 16, 20]
        totalFingers = 0
        if len(self.lmList) != 0:
            self.fingers = []

            # Thumb
            if self.lmList[self.tipIds[0]][1] < self.lmList[self.tipIds[0] - 1][1]:#It is for left hand. If you want to use it for right hand you have to change the comparator
                self.fingers.append(1)
            else:
                self.fingers.append(0)

            #Other four
            for id in range(1, 5):
                if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                    self.fingers.append(1)
                else:
                    self.fingers.append(0)

            totalFingers = self.fingers.count(1)
            cv2.putText(img, str(totalFingers), (575, 85), cv2.FONT_HERSHEY_PLAIN, 5, (255, 100, 100), 10)

        return totalFingers,img

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        totalFin,img = FingerCount.counter(FingerCount,img)
        print(totalFin)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            quit()

if __name__ == "__main__":
    main()
