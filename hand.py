#importing libraries
import cv2
import mediapipe as mp
import numpy as np
import random


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands 

capture = cv2.VideoCapture(0)
hands = mp_hands.Hands()   
wCam, hCam = 190, 380
handList = []
bot= ["Rock", "Scissors", "Paper"]
answer = False


def scissors(hand_landmarks):
    pointer_up = hand_landmarks.landmark[8].y < hand_landmarks.landmark[5].y
    middle_up = hand_landmarks.landmark[12].y < hand_landmarks.landmark[9].y
    other_down = all(
        hand_landmarks.landmark[tip].y > hand_landmarks.landmark[tip-2].y
        for tip in [16, 20]
    )
    thumb_down = hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x
    return pointer_up and middle_up and other_down and thumb_down


def rock(hand_landmarks):
    thumb_down = hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x
    other_down = all(
        hand_landmarks.landmark[tip].y > hand_landmarks.landmark[tip-2].y
        for tip in [8, 12, 16, 20]
    )
    return thumb_down and other_down


def paper(hand_landmarks):
    thumb_up = hand_landmarks.landmark[4].x < hand_landmarks.landmark[1].x
    other_up = all(
        hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip-2].y
        for tip in [8, 12, 16, 20]
    )
    return thumb_up and other_up


def bot():
    bot_answer = bot[random.randint(1,3)-1]
    return bot_answer


    


while True: 
    #points[2][21] (denna var i koden, jag vet inte vad denn gjorde doch och gav error)
    isTrue, image = capture.read()
    if not isTrue:
        break

    h, w, c = image.shape
    #FLIP THE image
    image = cv2.cvtColor(cv2.flip(image, 1),cv2.COLOR_BGR2RGB)
    #storing the results
    results = hands.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)



        
    player_answer = str()
    
    cv2.putText(image, 'CHOOSE: ROCK, PAPER OR SCISSORS', (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(image, '(Use your right hand, palm towards the camera)', (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
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

            if rock(hand_landmarks):
                cv2.putText(image, 'ROCK', (30, 420), cv2.FONT_HERSHEY_SIMPLEX, 3, (195, 0, 255), 2, cv2.LINE_AA)
                player_answer = "Rock"
            elif scissors(hand_landmarks):
                cv2.putText(image, 'SCISSORS', (30, 420), cv2.FONT_HERSHEY_SIMPLEX, 3, (188, 131, 124), 2, cv2.LINE_AA)
                player_answer = "Scissors"
            elif paper(hand_landmarks):
                cv2.putText(image, 'PAPER', (30, 420), cv2.FONT_HERSHEY_SIMPLEX, 3, (60, 20, 220), 2, cv2.LINE_AA)
                player_answer = "Paper"

            if answer == False:
                bot_answer = bot()
                answer = True
            
            print(bot_answer)




            


    cv2.imshow('Handtracker', image)
        
   
    



    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows

#string_hands = str(hand_landmarks) # flyttade ner kanske inte funkar
#    with open("hands.txt", "w", encoding="utf-8") as f:  #kanske inte funkar, flyttades ner
#        f.write(string_hands)