import cv2 as cv


# reading img
#img = cv.imread('images/hasse-haj.png')

#cv.imshow('Hasse Haj', img)

# reading videos

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('hoe', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows

#cv.waitKey(0)d

