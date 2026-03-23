#importing libraries
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands   #ändrade från videon (där hette det mphands)

string_hands = str(mp_hands)
#wCam, hCam = 190, 380d
with open("hands.txt", "w", encoding="utf-8") as f:  #funkar inte, fixa nästa lektion
    f.write(string_hands)

capture = cv2.VideoCapture(0)
hands = mp_hands.Hands()    #mphands
while True: 
    data, image = capture.read()
    #FLIP THE image
    image = cv2.cvtColor(cv2.flip(image, 1),cv2.COLOR_BGR2RGB)
    #storing the results
    results = hands.process(image)
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow('Handtracker', image)
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows

