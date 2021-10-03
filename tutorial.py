import cv2
import time
import datetime

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml")

detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5

frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

    # code for recording #############################
    # if len(faces) + len(bodies) > 0:
    #     if detection:
    #         timer_started = False
    #     else:
    #         detection = True
    #         current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    #         out = cv2.VideoWriter(
    #             f"{current_time}.mp4", fourcc, 20, frame_size)
    #         print("Started Recording!")
    # elif detection:
    #     if timer_started:
    #         if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
    #             detection = False
    #             timer_started = False
    #             out.release()
    #             print('Stop Recording!')
    #     else:
    #         timer_started = True
    #         detection_stopped_time = time.time()

    # if detection:
    #     out.write(frame)

    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)
        print(f"face detected x = {x} y= {y}")

    for (x, y, width, height) in eyes:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 3)
        print(f"eye detected x = {x} y= {y}")

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

# out.release()
cap.release()
cv2.destroyAllWindows()
