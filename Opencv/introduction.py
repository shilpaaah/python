import cv2

img=cv2.imread('/home/shilpa/Downloads/python/Opencv/friends.jpeg')

# print(img1.shape)    #h,w,channel
#resized_img=cv2.resize(img1,(500,300))
# grey_img = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
# (thresh,bw_img) = cv2.threshold(grey_img,200,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# print(thresh)
# cv2.imwrite('greyimage.jpg',grey_img) #save img
# cv2.imwrite('binary_img.jpg',bw_img)
img =cv2.rectangle(img,pt1=(8,145),pt2=(215,174),color=(0,0,255),thickness=cv2.FILLED)
img=cv2.circle(img,center=(188,159),radius=15,color=(255,0,0),thickness=-1)
img=cv2.putText(img,text='Friends',org=(20,168),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,
          color=(0,255,0),
          thickness=2
          )
cv2.imshow('image',img)#,bw_img)
cv2.waitKey()
cv2.destroyAllWindows()




