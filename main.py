import cv2
from DILPREET1910_Mediapipe import main
from UI import Button

##############################
# getting real time webcam feed
##############################
cap = cv2.VideoCapture(0)
detector = main.HandTracker(maxHands=1, detectionConfidence=0.5, trackingConfidence=0.5)

# defining buttons
buttonListValue = [['7', '8', '9', '/'],
                   ['4', '5', '6', '*'],
                   ['1', '2', '3', '-'],
                   ['0', '.', 'AC', '+']]
buttonList = []
for x in range(4):
    for y in range(4):
        xpos = x * 100 + 600
        ypos = y * 100 + 100
        buttonList.append(Button((xpos, ypos), 100, 100, buttonListValue[y][x]))
# defining buttons end


while True:
    success, frame = cap.read()
    frame = cv2.resize(frame, (1080, 720))
    frame = cv2.flip(frame, 1)

    #########################
    # drawing hand landmarks
    #########################
    # detect landmarks
    image, results = detector.findLandmarks(frame)
    # detect landmarks end

    # draw UI
    # input area
    cv2.rectangle(frame, (1000, 100), (600, 10), (255, 255, 255), cv2.FILLED)
    cv2.rectangle(frame, (1000, 100), (600, 10), (50, 50, 50), 3)
    cv2.putText(frame, "100 + 50 = 150", (600, 80), cv2.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)
    # buttons
    for button in buttonList:
        button.draw(frame)
    # equal to button
    cv2.rectangle(frame, (1000, 580), (600, 500), (215, 215, 215), cv2.FILLED)
    cv2.rectangle(frame, (1000, 580), (600, 500), (50, 50, 50), 3)
    cv2.putText(frame, "=", (790, 550), cv2.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)
    # draw UI end

    # draw landmarks
    if results.multi_hand_landmarks:
        detector.drawLandmarks(frame, results, False, 8, 12, True, True, 50)
        distance = detector.getDistance()
        print(distance)
    # draw landmarks end

    cv2.imshow("Raw web cam feed", frame)

    # defining when to close the webcam
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
