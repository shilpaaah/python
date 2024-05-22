import cv2
import HandTrackingModule as htm

detector = htm.handDetector()

cap = cv2.VideoCapture(0)
draw_color = (0,0,255)

while True:
    success,frame = cap.read()
    frame = cv2.resize(frame,(1280,720))
    frame = cv2.flip(frame,1)

    cv2.rectangle(frame,pt1=(20,10),pt2=(210,100),color=(0,0,255),thickness=-1)
    cv2.rectangle(frame,pt1=(230,10),pt2=(450,100),color=(0,255,0),thickness=-1)
    cv2.rectangle(frame,pt1=(470,10),pt2=(680,100),color=(0,255,255),thickness=-1)
    cv2.rectangle(frame,pt1=(700,10),pt2=(920,100),color=(255,0,255),thickness=-1)
    cv2.rectangle(frame,pt1=(940,10),pt2=(1260,100),color=(255,255,255),thickness=-1)
    cv2.putText(frame,"ERASER",(1000,60),cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(0,0,0),thickness=3)

#find hands and landmarks
    frame = detector.findHands(frame)
    lmlist = detector.findPosition(frame)
    #print(lmlist)
    if len(lmlist)!=0:

        #tip of fingers

        x1,y1 = lmlist[8][1:]
        x2,y2 =lmlist[12][1:]

# check which finger is up
        fingers = detector.fingersUp()
        #print(fingers)


# selection mode : 2 finger up condition (index finger & middle finger)
        if fingers[1] and fingers[2]:
            print('selection mode')

            if y1<=100:

                if 20<=x1<=210:
                    #print('red')
                    draw_color=(0,0,255)
                elif 230<=x1<=450:
                    #print('green')
                    draw_color=(0,255,0)
                elif 470<=x1<=680:
                    #print('yellow')
                    draw_color=(0,255,255)
                elif 700<=x1<=920:
                    #print('pink')
                    draw_color=(255,0,255)
                elif 940<=x1<=1260:
                    #print('eraser')
                    draw_color=(0,0,0)
            cv2.rectangle(frame,(x1,y1),(x2,y2),color=draw_color,thickness=-1)



# drawing mode : 1 finger up condition (index finger)
        if fingers[1] and not fingers[2]:
            print('drawing mode')

            cv2.circle(frame,(x1,y1),15,draw_color,thickness=-1)




    cv2.imshow('virtual painter',frame)
    if cv2.waitKey(1) & 0xFF ==27:
        break
cap.release()
cv2.destroyAllWindows