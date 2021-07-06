import pytesseract
import cv2
import json

class Word(object):
    def __init__(self, x:int, y:int, l:int, w:int, content:str):
        self.x = x
        self.y = y
        self.l = l
        self.w = w
        self.content = content
    def __repr__(self):
        return f"{self.content} at ({self.x}, {self,y}), dim = ({self.l}X{self.w})"

class Text(object):
    def __init__(self, words:list = []):
        self.words = words
    def __repr__(self):
        return ' '.join([f"{word.content}" for word in self.words])

if __name__ == "__main__":
    img = cv2.imread('test.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = pytesseract.image_to_data(img, lang='eng', nice=0, output_type=pytesseract.Output.DICT)
    print("*"*10)

    text = Text()
    for i in range(len(result['text'])):
        text.words.append(Word(
            result['left'][i],
            result['top'][i],
            result['width'][i],
            result['height'][i],
            result['text'][i]
            ))

    print(text)


    n_boxes = len(result['text'])
    for i in range(n_boxes):
        if int(result['conf'][i]) > 60:
            (x, y, w, h) = (result['left'][i], result['top'][i], result['width'][i], result['height'][i])
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imwrite(f"{i}_out.png", img)

   #cv2.imshow('img', img)
   #cv2.waitKey(0)
