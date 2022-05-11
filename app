#!/usr/local/bin/python

import pytesseract
import cv2
from libs import *
import argparse
import os

def get_args() -> tuple:
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="Path to input file")
    ap.add_argument("-o", "--output", required=True, help="Path to output file")
    ap.add_argument("-w", "--word", required=True, help="Word to search")
    args = vars(ap.parse_args())

    ipath = os.path.abspath(args["input"])
    opath = os.path.abspath(args["output"])
    word  = args['word']

    return (ipath, opath, word)

def main() -> ():
    ipath,  opath, word = get_args()
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
        if float(result['conf'][i]) > 60 and text.words[i].content == word:
            (x, y, dx, dy) = text.words[i].x, text.words[i].y, text.words[i].dx, text.words[i].dy
            img = cv2.rectangle(img, (x - 2, y - 2), (x + dx + 2, y + dy + 2), (0, 0, 255), 2)

    breakpoint()
    cv2.imwrite(opath, img)

if __name__ == "__main__":
    main()
