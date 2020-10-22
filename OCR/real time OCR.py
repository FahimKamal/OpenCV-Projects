import cv2
import pytesseract

camera = cv2.VideoCapture(0)

def readText(img):
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ### Detecting Words
    # print(pytesseract.image_to_boxes(img))
    imageHeight, imageWidth, _ = img.shape
    boxes = pytesseract.image_to_data(rgb)

    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            if len(b) == 12:
                # print(b)
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
                # cv2.putText(img, b[11], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (50, 50, 255), 1)

    text = pytesseract.image_to_string(rgb)
    print(text)
    with open('output.txt', 'w') as file:
        file.write(text)
    file.close()

    while True:
        cv2.imshow('Camera', img)
        key = cv2.waitKey(10)
        # Pressing esc will terminate the program
        if key == 27:
            break


while True:
    _, img = camera.read()
    cv2.imshow('Camera', img)

    key = cv2.waitKey(10)
    # Pressing esc will terminate the program
    if key == 27:
        break
    # if space is pressed read the the text
    elif key == 32:
        readText(img)
