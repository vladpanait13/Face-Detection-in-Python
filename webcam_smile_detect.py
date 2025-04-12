import cv2
import urllib.request

# URLs for Haar cascades
face_url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
smile_url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_smile.xml"

# Download face cascade
with open("temp_face.xml", "wb") as f:
    f.write(urllib.request.urlopen(face_url).read())

# Download smile cascade
with open("temp_smile.xml", "wb") as f:
    f.write(urllib.request.urlopen(smile_url).read())

# Load classifiers
face_cascade = cv2.CascadeClassifier("temp_face.xml")
smile_cascade = cv2.CascadeClassifier("temp_smile.xml")

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 100, 255), 2)
        face_roi_gray = gray[y:y + h, x:x + w]
        face_roi_color = frame[y:y + h, x:x + w]

        smiles = smile_cascade.detectMultiScale(face_roi_gray, scaleFactor=1.7, minNeighbors=22)

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(face_roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)
            cv2.putText(frame, 'Smiling 😊 !', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            break # Only show one smile per face for clarity

        cv2.imshow("Smile Detection - Press 'q' to Quit", frame)

        key = cv2.waitKey(1)
        if key == ord('q') or key == 27: # Press 'q' or ESC to quit
            break

cap.release()
cv2.destroyAllWindows()