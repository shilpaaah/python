import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawings = mp.solutions.drawing_utils

hands = mp_hands.Hands() #no parameters need to pass bcz the static mode is False by default.

video = cv2.VideoCapture(0)

while True:
    success,frame=video.read()
    results = hands.process(frame)

    print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
      
      for hand_no,hand_land_marks in enumerate(results.multi_hand_landmarks):
         mp_drawings.draw_landmarks(image=frame,landmark_list=hand_land_marks,connections=mp_hands.HAND_CONNECTIONS)


    cv2.imshow('video reader',frame)
    if cv2.waitKey(1)&0xFF==27:  #0xFF escape button
       break
video.release() # used to stop the video
cv2.destroyAllWindows()
       