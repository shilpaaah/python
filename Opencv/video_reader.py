import cv2

video=cv2.VideoCapture(0)   # if we gave a videopath then video will play if 0 then webcam will open
while True:
    success,frame=video.read()
    #grey_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #(thresh,bw_img)=cv2.threshold(grey_img,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    grey_img=cv2.rectangle(frame,pt1=(8,145),pt2=(215,174),color=(0,0,255),thickness=cv2.FILLED)
    print(success)

    cv2.imshow('video_reader',grey_img)
    if cv2.waitKey(1) & 0xFF==27:
        break
video.release()
cv2.destroyAllWindows()