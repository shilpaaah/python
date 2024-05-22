import cv2
img1=cv2.imread('/home/shilpa/Downloads/python/Opencv/image1.jpeg')
#img2=cv2.imread('/home/shilpa/Downloads/python/Face Detection/13reasonswhy.jpeg')

eyecascade=cv2.CascadeClassifier('/home/shilpa/Downloads/python/Face Detection/haarcascade_eye.xml')

grey_img = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

# pass grey img to face_cascade

eyes = eyecascade.detectMultiScale(grey_img)    # coordinates can be saved here.

print(eyes)

# to draw rectangles on all the eyes : we create a loop:
for (x,y,w,h) in eyes:
    cv2.rectangle(img1,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,0),thickness=3)

cv2.imshow('eyeimage',img1)
cv2.waitKey(5000)
cv2.destroyAllWindows()