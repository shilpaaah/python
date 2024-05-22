import mediapipe as mp
import cv2

img=cv2.imread('/home/shilpa/Downloads/python/handtracking/hand1.jpg')

rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  # convert BGR to RCB

mp_hands = mp.solutions.hands

mp_drawings = mp.solutions.drawing_utils  #to draw lines

hands = mp_hands.Hands(static_image_mode=True,max_num_hands=2)
result = hands.process(rgb_img)

print(result.multi_handedness)

print(result.multi_hand_landmarks)   # print landmark coordinates

if result.multi_hand_landmarks:

    #this is to remove error while the hands are not detected
    for hand_no,hand_land_marks in enumerate(result.multi_hand_landmarks):
        mp_drawings.draw_landmarks(image=img,landmark_list=hand_land_marks,connections=mp_hands.HAND_CONNECTIONS)


cv2.imshow('hand_tracking',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()