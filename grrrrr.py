import cv2 as cv
import numpy as np



# reading img
img = cv.imread('images/hasse-haj.png')

#

# reading videos

capture = cv.VideoCapture(0)



while True:


# concatenate image Horizontally
    Hori = np.concatenate((capture, img), axis=1)
# concatenate image Vertically
    Verti = np.concatenate((capture, img), axis=0)
    isTrue, frame = capture.read()
    cv.imshow('hoe', Hori)
    cv.imshow('Hasse Haj', Verti)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows

#cv.waitKey(0)d

