import pytesseract
import cv2
from libs import *
import argparse
import os

def get_args() -> dict:
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="Path to input file")
    ap.add_argument("-o", "--output", required=True, help="Path to output file")
    args = vars(ap.parse_args())

    ipath = os.path.abspath(args["input"])
    opath = os.path.abspath(args["output"])

    return ipath, opath

def main() -> ():
    ipath,  opath = get_args()
    img = cv2.imread(ipath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

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
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imwrite(f"{i}_out.png", img)

if __name__ == "__main__":
    main()
