import cv2
from pyzbar.pyzbar import decode
import time

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

used_code = []

camera = True

while camera == True:
    success, frame = cap.read()

    for code in decode(frame):
        if code.data.decode('utf-8') not in used_code:
            print('Approve and enter')
            print(code.data.decode('utf-8'))
            used_code.append(code.data.decode('utf-8'))
            time.sleep(2)

        elif code.data.decode('utf-8') in used_code:
            print('Already use')

    cv2.imshow('Decode', frame)
    cv2.waitKey(1)