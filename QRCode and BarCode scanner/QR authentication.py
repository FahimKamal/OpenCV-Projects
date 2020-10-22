import cv2
import numpy as np
from pyzbar.pyzbar import decode

camera = cv2.VideoCapture(0)
# Width
camera.set(3, 640)
# Height
camera.set(4, 480)

# read the authentication file
with open('mydata.txt', 'r') as f:
    mydatalist = f.read().splitlines()

print(mydatalist)
while True:
    success, img = camera.read()
    for qrcode in decode(img):
        mydata = qrcode.data.decode('utf-8')
        print(mydata)

        if mydata in mydatalist:
            print(f'{mydata} is Authorized')
            output = 'Authorized'
            color = (0, 255, 0)
        else:
            print(f'{mydata} is Un-authorized')
            output = 'Un-authorized'
            color = (255, 0, 0)
        pts = np.array([qrcode.polygon], np.int32)
        pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, color, 5)
        pts2 = qrcode.rect
        cv2.putText(img, output, (pts2[0], pts2[1]),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow('Camera', img)
    key = cv2.waitKey(10)
    # Pressing esc will terminate the program
    if key == 27:
        break
