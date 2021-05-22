# face clasifier sunt antrenate cu imagii ce contin fete

import cv2
import winsound

pedestrian_cascade = cv2.CascadeClassifier('pedestrian.xml')
duration = 1000  # milliseconds
freq = 440  # Hz

cap = cv2.VideoCapture('zebra.mp4')

# pt mp4
while cap.isOpened():
    _, img = cap.read()
    detected = False
    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # viteza de redare 1.2
    pedestrian = pedestrian_cascade.detectMultiScale(gray, 1.2, 4)

    for (x, y, w, h) in pedestrian:

        if(h>100 and w>100):
            detected = True
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
        else:
            detected = False

    if detected == True:
        winsound.Beep(freq, duration)
        cv2.putText(img, "Don't kill the pedestrian!!!", (x-250 , y - 200), cv2.FONT_ITALIC, 1.5, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('Show mercy!', img)
    # cv2.waitKey() #fara asta la video

    key = cv2.waitKey(20)
    if key == 27:  # exit on ESC
        break

cap.release
