import cv2;

trained_car_data = cv2.CascadeClassifier('haarcascade_car.xml')

#! For Images
# car_image = cv2.imread('./car-image.png')

# greyscaled_image = cv2.cvtColor(car_image, cv2.COLOR_BGR2GRAY)

# car_coordinates = trained_car_data.detectMultiScale(greyscaled_image)

# for (x, y, w, h) in car_coordinates:
#     cv2.rectangle(car_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# cv2.imshow('Car Detector', car_image)

# cv2.waitKey()

#! For Videos
car_video = cv2.VideoCapture('https://www.youtube.com/watch?v=d4L1Pte7zVc')

while True:
    successfull_frame_read, frame = car_video.read()
    greyscaled_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    car_coordinates = trained_car_data.detectMultiScale(greyscaled_video)
    for (x, y, w, h) in car_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('Car Detector', frame)
    key = cv2.waitKey(1)
    if key == 81 or key == 113:
        break

webcam.release()

print('Code completed!')