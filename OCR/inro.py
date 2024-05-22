import cv2
import pytesseract
from pytesseract import Output

img=cv2.imread('/home/shilpa/Downloads/python/OCR/sarcs.png')

text=pytesseract.image_to_string(img)
data= pytesseract.image_to_data(img,output_type=Output.DICT)
print(data['text'])
print(data['left'])
#print(data.keys())
#print(data['conf'])
#print(text)

n_boxes=len(data['text'])   #to check how many box we need.
print(n_boxes)    #17


cv2.imshow('ocr',img)
cv2.waitKey()
cv2.destroyAllWindows()