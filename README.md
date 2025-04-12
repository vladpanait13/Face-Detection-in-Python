# Face Detection with OpenCV

This project demonstrates how to perform face detection in images using Python and OpenCV's Haar cascade classifiers. The script downloads the pre-trained classifier, processes a local image or webcam feed, detects faces, and displays the result with bounding boxes.

## 🔍 Features

- Downloads the Haar cascade classifier directly from the OpenCV GitHub repository.
- Supports both image-based and webcam-based face detection.
- Converts input to grayscale for optimized processing.
- Detects frontal faces and draws rectangles around them.
- Displays the result in a resizable window.

## 🛠️ Requirements

Make sure you have the following Python packages installed:

```bash
pip install opencv-python numpy
```

## 📁 Project Structure

├── image.jpg               # Input image (optional if using webcam)

├── temp_face.xml           # Haar cascade XML file (downloaded automatically)

├── face_detect.py          # Script for image face detection

├── webcam_detect.py        # Script for real-time face detection using webcam

├── webcam_smile_detect.py  # Script for real-time face and smile detection using webcam

└── README.md               # Project documentation


## 🚀 How to Use

### 📷 Face Detection on Image

1. Place your input image in the project directory and name it image.jpg.
    (Or modify the script to use a different image file.)

2. Run the image detection script:

```
python app.py
```

3. A window will open displaying the image with detected faces. Press any key to close it.

### 🎥 Real-Time Face Detection via Webcam

1.    Ensure your webcam is connected and accessible.

2.    Run the webcam detection script:

```
python webcam_detect.py
```

3.    A real-time video feed will appear with faces detected in live frames.
    Press the q key to quit.

## 🧠 How It Works

    The Haar cascade XML is downloaded at runtime from OpenCV's GitHub.

    Input (image or webcam frame) is converted to grayscale.

    The classifier scans the input for facial features.

    Detected faces are highlighted with red rectangles.

### 😄 Smile Detection (Image & Webcam)

In addition to face detection, the project also detects smiles using Haar cascades.

#### 💡 How It Works

    After detecting a face, a region of interest (ROI) is extracted from the face area.

    A separate Haar cascade classifier (haarcascade_smile.xml) is applied to the ROI.

    If a smile is detected, it's highlighted with a different color box (or labeled).

#### 🧪 Run Smile Detection on Webcam
```
python webcam_smile_detect.py
```
