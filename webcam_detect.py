import cv2
import urllib.request

# Download Haar cascade if not already present
url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
resp = urllib.request.urlopen(url)
with open("temp_face.xml", "wb") as f:
    f.write(resp.read())

# Load classifier 
face_cascade = cv2.CascadeClassifier("temp_face.xml")

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 100, 255), 2)

    cv2.imshow("Webcam Face Detection - Press 'q' to Quit", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()