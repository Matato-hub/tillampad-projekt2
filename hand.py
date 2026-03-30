#importing libraries
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands   #ändrade från videon (där hette det mphands)

capture = cv2.VideoCapture(0)
hands = mp_hands.Hands()    #mphands



#wCam, hCam = 190, 380d



while True: 
    data, image = capture.read()
    h, w, c = image.shape
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
        # Loopa igenom varje enskild punkt (0-21) i handen
            for id, lm in enumerate(hand_landmarks.landmark):
                # lm.x och lm.y är normaliserade (0.0 till 1.0)
                # Här räknar vi om dem till pixlar:
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                print(f"Landmark {id}: x={cx}, y={cy}")
    cv2.imshow('Handtracker', image)
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows

#string_hands = str(hand_landmarks) # flyttade ner kanske inte funkar
#    with open("hands.txt", "w", encoding="utf-8") as f:  #kanske inte funkar, flyttades ner
#        f.write(string_hands)