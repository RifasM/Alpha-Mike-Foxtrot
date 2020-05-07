import numpy as np
import cv2

cap = cv2.VideoCapture("met.mp4")
i = 1

while cap.read():
    ret, frame1 = cap.read()
    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    # gray = cv2.addWeighted(gray, 0.1, gray, 0, 1)

    ret, thresh = cv2.threshold(gray, 200, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    gray = cv2.drawContours(gray, contours, -1, (0, 255, 0), -1)
    if len(contours) != 0:
        x = max(max(contours, key=cv2.contourArea), key=cv2.contourArea)[0][0]
        y = max(max(contours, key=cv2.contourArea), key=cv2.contourArea)[0][1]
        # print(x, y, frame1.shape[0], frame1.shape[1] )
        if x*y > 0.2*(frame1.shape[0] * frame1.shape[1]):
            print("Metal Spill", str(i))
            cv2.imwrite('images/opticalfb' + str(i) + '.png', frame1)
            cv2.imwrite('images/opticalhsv' + str(i) + '.png', gray)
            i += 1

    # cv2.addWeighted(gray, contrast, gray, 0, brightness)
    # gray = cv2.GaussianBlur(gray, (11, 11), 0)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    cv2.circle(gray, maxLoc, 40, (255, 255, 0), 2)

    cv2.imshow("Grey", gray)
    cv2.imshow("Frame", frame1)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
