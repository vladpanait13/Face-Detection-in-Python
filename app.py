import cv2
import numpy as np 
import urllib.request

# Download the xml classifier
url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
resp = urllib.request.urlopen(url)
xml_data = resp.read()

# Create XML file
with open("temp_face.xml", "wb") as f:
    f.write(xml_data)

# Load image
img = cv2.imread("image.jpg") 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load classifier
face_cascade = cv2.CascadeClassifier("temp_face.xml")

# Detect faces 
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw square
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (155, 0, 0), 2)

# Show the image
cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()