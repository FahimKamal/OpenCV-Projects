import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('sample2.jpg')
# codes = decode(img)
# print(codes)
for code in decode(img):
#     # binary data
#     print(code.data)
#     # Actual data
#     print(code.data.decode('utf-8'))
#     print(code.type)
#     print(code.rect)
    print(code.polygon)
    pts = np.array([code.polygon], np.int32)
    pts.reshape((-1, 1, 2))
    print(pts)

camera = cv2.VideoCapture(0)
# Width
camera.set(3, 640)
# Height
camera.set(4, 480)

while True:
    success, img = camera.read()
    for qrcode in decode(img):
        mydata = qrcode.data.decode('utf-8')
        print(mydata)
        pts = np.array([qrcode.polygon], np.int32)
        pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255, 0, 255), 5)
        pts2 = qrcode.rect
        cv2.putText(img, mydata, (pts2[0], pts2[1]),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
    
    cv2.imshow('Camera', img)
    key = cv2.waitKey(10)
    # Pressing esc will terminate the program
    if key == 27:
        break
