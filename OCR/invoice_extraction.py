import cv2
import pytesseract
from pytesseract import Output
import re

img=cv2.imread('/home/shilpa/Downloads/python/OCR/invoice.jpeg')

text=pytesseract.image_to_string(img)
data= pytesseract.image_to_data(img,output_type=Output.DICT)
print(data['text'])
print(data['left'])
print(data.keys())
print(data['conf'])
print(text)

n_boxes=len(data['text'])   #to check how many box we need.
print(n_boxes)    #17

date_pattern='^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'
mail_pattern =	'^[a-z0-9](\.?[a-z0-9]){5,}@example\.net$'

for i in range(n_boxes):
    if data['conf'][i]>60:
           if re.match(mail_pattern,data['text'][i]) or re.match(date_pattern,data['text'][i]):
     

                x,y,w,h=data['left'][i],data['top'][i],data['width'][i],data['height'][i]
                print(x,y,w,h)
                cv2.rectangle(img,(x,y),(x+w,y+h),color=(255,255,0),thickness=3)
 
cv2.imshow('ocr',img)
cv2.waitKey()
cv2.destroyAllWindows()