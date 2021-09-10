import cv2
import numpy as np
import math
import serial
import time

ser = serial.Serial('COM3', baudrate = 9600, timeout = 1)

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

#hsv lower and upper values for a yellow ball used for testing. Values found using trackbars.
path_lower = np.array([115,35,60])
path_upper = np.array([133,255,255])

font = cv2.FONT_HERSHEY_COMPLEX
kernel = np.ones((5,5),np.uint8)

r = 1

while True:
    ret, frame = cap.read()
    if not ret:
        cap = cv2.VideoCapture(0)
        continue
    (h, w) = frame.shape[:2]
    blur = cv2.GaussianBlur(frame,(5,5),cv2.BORDER_DEFAULT)
    hsvvid = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    #command = input("f/b/r/l: ")
    #ser.write(command.encode())

    path_mask = cv2.inRange(hsvvid, path_lower, path_upper)
    opening = cv2.morphologyEx(path_mask, cv2.MORPH_OPEN, kernel)
    erosion = cv2.erode(opening,kernel,iterations = 1)
    dilation = cv2.dilate(erosion,kernel,iterations = 5)
    path_contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, path_contours, -1, (0,255,0), 3)

    if len(path_contours) > 0:
        largest = max(path_contours, key = cv2.contourArea)
        x_2, y_2, w_2, h_2 = cv2.boundingRect(largest)
        cv2.rectangle(frame, (x_2, y_2), (x_2 + w_2, y_2 + h_2), (0, 0, 255), 3)
        error = x_2 + (w_2/2) - w/2
        #cv2.putText(frame, str(error), (5, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)

        blackbox = cv2.minAreaRect(largest)
        (x_min, y_min), (w_min, h_min), ang = blackbox
        if ang > 45:
            ang = ang - 90
        if w_min < h_min and ang < 0:
            ang = 90 + ang
        if w_min > h_min and ang > 0:
            ang = ang - 90
        ang = int(ang)
        box = cv2.boxPoints(blackbox)
        box = np.int0(box)
        cv2.drawContours(frame, [box], 0, (0,0,255), 3)
        cv2.putText(frame, str(ang), (5, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)
        #cv2.putText(frame, str(a_delay), (5, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('path video', frame)
    key = cv2.waitKey(1)
    if key == 27: #press esc to exit
        break

cap.release()
cv2.destroyAllWindows()
