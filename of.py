"""
Optical Flow Algo
"""

import cv2
import numpy as np
cap = cv2.VideoCapture("video_Trim.mp4")

ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[..., 1] = 255

i = 1

while True:
    ret, frame2 = cap.read()
    next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale", next)

    flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    hsv[..., 0] = ang*180/np.pi/2
    hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
    rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    avg_color_per_row = np.average(np.average(rgb, axis=0), axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)
    # print(avg_color)

    if avg_color > 12:
        print("Fall "+str(i)+" Detected")
        cv2.imwrite('images/opticalfb'+str(i)+'.png', frame2)
        cv2.imwrite('images/opticalhsv'+str(i)+'.png', rgb)
        i += 1

    cv2.imshow('Video', frame2)
    cv2.imshow('HSV', rgb)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite('opticalfb.png', frame2)
        cv2.imwrite('opticalhsv.png', rgb)
    prvs = next

cap.release()
cv2.destroyAllWindows()


# TODO: Obtain Object Sizes and calculate speed
# TODO: Direction of movement of object
# TODO: Bounding box for falling objects
