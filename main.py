import cv2
import mediapipe as mp
import pyautogui
import math
video=cv2.VideoCapture(0)
screen_w,screen_h=pyautogui.size()
mp_drawing=mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles
mp_hands=mp.solutions.hands
hands=mp_hands.Hands(static_image_mode=True,max_num_hands=2,min_detection_confidence=0.5,min_tracking_confidence=0.5)
while True:
    r,frame=video.read()
    if r==True:
        frame=cv2.flip(frame,1)
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=hands.process(frame)
        frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            h,w,c=frame.shape
            index=landmarks.landmark[8]
            thumb=landmarks.landmark[4]
            x=int(index.x*w)
            y=int(index.y*h
            mouse_x=int(index.x*screen_w)
            mouse_y=int(index.y*screen_h)
            pyautogui.moveTo(mouse_x,mouse_y)
            tx=int(thumb.x*w)
            ty=int(thumb.y*h)
            distance=math.hypot(x-tx,y-ty)
            if distance <40:
                pyautogui.click()
            cv2.circle(frame,(x,y),10,(0,0,255),2)

            mp_drawing.draw_landmarks(frame,landmarks,mp_hands.HAND_CONNECTIONS)
    if cv2.waitKey(25) & 0xff==ord("p"):
        break
    cv2.imshow("frame",frame)

video.release()
cv2.destroyAllWindows()