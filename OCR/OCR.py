import cv2
import pytesseract

img = cv2.imread('ocr-test1.png')
img = cv2.resize(img, (800, 500))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img))

# ### Detecting Characters
# # print(pytesseract.image_to_boxes(img))
# imageHeight, imageWidth, _ = img.shape
# boxes = pytesseract.image_to_boxes(img)
#
# for b in boxes.splitlines():
#     b = b.split()
#     print(b)
#     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#     cv2.rectangle(img, (x, imageHeight - y), (w, imageHeight- h), (0, 0, 255), 1)
#     cv2.putText(img, b[0], (x, imageHeight- y-35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (50, 50, 255), 1)

### Detecting Words
# print(pytesseract.image_to_boxes(img))
imageHeight, imageWidth, _ = img.shape
boxes = pytesseract.image_to_data(img)

for x, b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        if len(b) == 12:
            print(b)
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 1)
            cv2.putText(img, b[11], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (50, 50, 255), 1)


cv2.imshow('Result', img)
cv2.waitKey(0)