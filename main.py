import pytesseract
import cv2
import json

if __name__ == "__main__":
    img = cv2.imread('test.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = pytesseract.image_to_data(img, lang='eng', nice=0, output_type=pytesseract.Output.DICT)
    print("*"*10)
    
   # for key in result.keys():
   #     print(f"length for {key} --> {len(result[key])}")
   
    keys = result.keys()
    print(keys)
    for i, word in enumerate(result['text']):
        
        p = (p := f'{word} has')
        for key in keys:
           p = p + f" {key} = {result[key][i]}"

        print(p)
