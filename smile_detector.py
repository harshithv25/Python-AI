import cv2
import random

trained_face_data = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')
trained_smile_data = cv2.CascadeClassifier('haarcascade_smile.xml')
trained_eye_data = cv2.CascadeClassifier('haarcascade_eye.xml')

# colored_image = cv2.imread('./mrbeast.png')

# greyscaled_image = cv2.cvtColor(colored_image, cv2.COLOR_BGR2GRAY)

# face_coordinates = trained_smile_data.detectMultiScale(greyscaled_image)

# for (x, y, w, h) in face_coordinates:
#     B = random.randint(0, 255)
#     G = random.randint(0, 255)
#     R = random.randint(0, 255)
#     cv2.rectangle(colored_image, (x, y), (x + w, y + h), (B, G, R), 2)


def detect(gray, frame):

    return frame


webcam = cv2.VideoCapture(0)

while True:
    successfull_frame_read, frame = webcam.read()

    greyscaled_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(
        greyscaled_image, 1.3, 5)
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        smiles = trained_smile_data.detectMultiScale(greyscaled_image, 1.8, 20)

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(smile_color, (sx, sy),
                          ((sx + sw), (sy + sh)), (0, 0, 255), 2)

    cv2.imshow('Face Detector', frame)
    key = cv2.waitKey(1)
    if key == 81 or key == 113:
        break

webcam.release()

# cv2.imshow('Face Detector', colored_image)

# cv2.waitKey()

print('Code completed')
