#importing libraries
import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands   #ändrade från videon (där hette det mphands)

capture = cv2.VideoCapture(0)
hands = mp_hands.Hands()    #mphands
wCam, hCam = 190, 380
handList = []

def scissors(hand_landmarks):
    pointer_up = hand_landmarks.landmark[8].y < hand_landmarks.landmark[5].y
    middle_up = hand_landmarks.landmark[12].y < hand_landmarks.landmark[9].y
    other_down = all(
        hand_landmarks.landmark[tip].y > hand_landmarks.landmark[tip-2].y
        for tip in [16, 20]
    )
    thumb_down = hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x
    return pointer_up and middle_up and other_down and thumb_down


while True: 
   # points[2][21] (denna var i koden, jag vet inte vad denn gjorde doch och gav error)
    data, image = capture.read()
    h, w, c = image.shape
    #FLIP THE image
    image = cv2.cvtColor(cv2.flip(image, 1),cv2.COLOR_BGR2RGB)
    #storing the results
    results = hands.process(image)
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

    cv2.putText(image, 'CHOOSE: ROCK, PAPER OR SCISSORS', (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(image, 'YOU HAVE CHOSEN:', (30,350), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks, mp_hands.HAND_CONNECTIONS)
        # Loopa igenom varje enskild punkt (0-21) i handen
            for id, lm in enumerate(hand_landmarks.landmark):
                # lm.x och lm.y är normaliserade (0.0 till 1.0)
                # Här räknar vi om dem till pixlar:
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                print(f"Landmark {id}: x={cx}, y={cy}")
            if scissors(hand_landmarks):
                cv2.putText(image, 'SCISSORS', (30, 370), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 195), 2, cv2.LINE_AA)       
    cv2.imshow('Handtracker', image)
    
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows

#string_hands = str(hand_landmarks) # flyttade ner kanske inte funkar
#    with open("hands.txt", "w", encoding="utf-8") as f:  #kanske inte funkar, flyttades ner
#        f.write(string_hands)