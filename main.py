import pytesseract
import cv2
import json
from libs import *

if __name__ == "__main__":
    img = cv2.imread('test.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = pytesseract.image_to_data(img, lang='eng', nice=0, output_type=pytesseract.Output.DICT)
    print("*"*10)

    text = Text()
    for i in range(len(result['text'])):
        text + Word(
            result['left'][i],
            result['top'][i],
            result['width'][i],
            result['height'][i],
            result['text'][i]
            )

    print(text)
    n_boxes = len(text)
    for i in range(n_boxes):
        if int(result['conf'][i]) > 60:
            (x, y, w, h) = (result['left'][i], result['top'][i], result['width'][i], result['height'][i])
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imwrite(f"{i}_out.png", img)
