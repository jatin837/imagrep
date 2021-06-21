import cv2
import pytesseract

class letter(object):
    def __init__(this, 

img = cv2.imread('test.png')

h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img) 

    
# This is the method to get boxes around text in image
# splitline is used for string
# does that means boxes is a string?
#for b in boxes.splitlines():
#    b = b.split(' ')
#    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

print(type(boxes))
#cv2.imshow('img', img)
#cv2.waitKey(0) 
