import pytesseract
import cv2
import json

if __name__ == "__main__":
    img = cv2.imread('test.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = pytesseract.image_to_data(img, lang='eng', nice=0, output_type=pytesseract.Output.DICT)
    with open("out.json", 'w') as f:
        json.dump(result, f, indent = 2)
    print(result)
    print("*"*10)
    print(result.keys())
