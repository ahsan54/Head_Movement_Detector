# detector.py
import cv2
import dlib
from twilio.rest import Client

account_sid = 'Your Acc  Sid'
auth_token = 'Your Auth token'
client = Client(account_sid, auth_token)

def send_whatsapp_message(message):
    message = client.messages.create(
        from_='whatsapp: Your twilio whatsapp number',
        body=message,
        to='whatsapp: Your target number'
    )
    return message.sid

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("your Model for face movement detection")

cap = cv2.VideoCapture(0)  

prev_nose_x = None
prev_nose_y = None

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)

        # Get the coordinates of the nose (landmark point 30)
        nose_x = landmarks.part(30).x
        nose_y = landmarks.part(30).y

        if prev_nose_x is not None and prev_nose_y is not None:
            # Calculate the change in nose position
            dx = abs(nose_x - prev_nose_x)
            dy = abs(nose_y - prev_nose_y)

            # If the change exceeds a threshold, consider it a head movement
            if dx > 5 or dy > 5:
                print("Head movement detected!")
                send_whatsapp_message("your Desired Reminder")
                prev_nose_x = nose_x
                prev_nose_y = nose_y
        else:
            prev_nose_x = nose_x
            prev_nose_y = nose_y

    cv2.imshow('Head Movement Detection', frame)

    if cv2.waitKey(30) & 0xFF == 27: # Esc key to close
        break

cap.release()
cv2.destroyAllWindows()
