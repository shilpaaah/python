import cv2
#img1=cv2.imread('/home/shilpa/Downloads/python/Face Detection/friends.jpeg')
img2=cv2.imread('/home/shilpa/Downloads/python/Face Detection/13reasonswhy.jpeg')

facecascade=cv2.CascadeClassifier('/home/shilpa/Downloads/python/Face Detection/haarcascade_frontalface_default.xml')

grey_img = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# pass grey img to face_cascade

faces = facecascade.detectMultiScale(grey_img)    # coordinates can be saved here.

print(faces)

# to draw rectangles on all the faces : we create a loop:
for (x,y,w,h) in faces:
    cv2.rectangle(img2,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,0),thickness=3)

cv2.imshow('faceimage',img2)
cv2.waitKey(5000)
cv2.destroyAllWindows()