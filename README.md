# 👁️ Eye Controlled Mouse Pointer

## Project Overview

Eye Controlled Mouse Pointer is an AI-powered computer vision application that enables users to control the mouse cursor using eye movements detected through a webcam. The system tracks facial landmarks and eye positions in real time, allowing users to move the cursor, perform clicks, and interact with the computer without using a physical mouse.

Built using Python, OpenCV, MediaPipe, and PyAutoGUI, this project demonstrates the practical implementation of eye tracking, facial landmark detection, and human-computer interaction technologies to create an accessible and touch-free computer control system.

---

## Features

* Real-Time Eye Tracking
* Eye-Based Cursor Movement
* Blink Detection for Mouse Clicks
* Facial Landmark Detection
* Hands-Free Computer Control
* Live Webcam Tracking
* Accurate Eye Position Recognition
* Touchless User Interaction
* Lightweight and Fast Performance
* Accessibility Support

---

## Technologies Used

* Python
* OpenCV
* MediaPipe
* PyAutoGUI
* NumPy
* Computer Vision

---

## Project Structure

Eye-Controlled-Mouse-Pointer/

├── main.py

├── eye_tracker.py

├── mouse_controller.py

├── blink_detector.py

├── requirements.txt

├── .gitignore

└── README.md

---

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/eye-controlled-mouse-pointer.git

cd eye-controlled-mouse-pointer
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python main.py
```

### 6. Allow Webcam Access

The application will access the webcam and begin tracking eye movements.

---

## System Workflow

### Eye Detection

* Capture live webcam feed.
* Detect facial landmarks.
* Identify eye regions.
* Track eye movement in real time.

### Cursor Control

* Map eye positions to screen coordinates.
* Move mouse pointer based on eye movement.
* Track gaze direction accurately.
* Provide smooth cursor navigation.

### Click Detection

* Detect eye blinks.
* Convert blink actions into mouse clicks.
* Support hands-free interaction.
* Improve accessibility and usability.

---

## Core Modules

### Eye Tracking Module

* Webcam Access
* Eye Detection
* Gaze Tracking
* Facial Landmark Detection

### Cursor Control Module

* Cursor Position Mapping
* Mouse Movement
* Screen Navigation
* Real-Time Tracking

### Blink Detection Module

* Blink Recognition
* Mouse Click Actions
* Gesture Processing
* Event Handling

### User Interface Module

* Webcam Display
* Eye Tracking Visualization
* Status Monitoring
* Performance Feedback

---

## Requirements

```text
OpenCV-Python
MediaPipe
PyAutoGUI
NumPy
```

Install all requirements using:

```bash
pip install -r requirements.txt
```

---

## Future Enhancements

* Eye Gesture Commands
* Scroll Control Using Eye Movements
* Multi-Monitor Support
* Custom Click Gestures
* Voice Command Integration
* AI-Based Gaze Prediction
* Desktop GUI Dashboard
* Accessibility Enhancements

---

## Author

Developed by: Barnali Bhowmik

---

## License

This project is created for educational and learning purposes. Feel free to modify and improve it as needed.

⭐ If you find this project useful, please give it a star.
