import cv2
import pytesseract
from pytesseract import Output

img=cv2.imread('/home/shilpa/Downloads/python/OCR/Untitled55.png')

text=pytesseract.image_to_string(img)
data= pytesseract.image_to_data(img,output_type=Output.DICT)
print(data['text'])
print(data['left'])
#print(data.keys())
print(data['conf'])
#print(text)

n_boxes=len(data['text'])   #to check how many box we need.
print(n_boxes)    #17

for i in range(n_boxes):
    if data['conf'][i]>=60:
     

           x,y,w,h=data['left'][i],data['top'][i],data['width'][i],data['height'][i]
           print(x,y,w,h)
           cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,255,0),thickness=5)

cv2.imshow('ocr',img)
cv2.waitKey()
cv2.destroyAllWindows()