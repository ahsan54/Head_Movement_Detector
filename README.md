# Head_Movement_Detector

# Face Motion Detector

This project detects head movements using a webcam and sends a WhatsApp message via Twilio Web Api to desired number when head movement is detected.

What is Face Motion Detector?
Face Motion Detector is a Python-based application that uses computer vision to detect head movements through a webcam. It utilizes the dlib library for facial landmark detection and OpenCV for video capture and processing. When a head movement is detected, the application sends a WhatsApp message using the Twilio API. This can be particularly useful for applications such as monitoring attention, detecting drowsiness, or any other scenario where detecting head motion is essential.

Key Features:
Real-time Head Movement Detection: Uses a webcam to monitor and detect head movements in real-time.
Facial Landmark Detection: Employs dlib's pre-trained facial landmark model to accurately locate facial features.
WhatsApp Notifications: Sends a WhatsApp message through Twilio's API when a head movement is detected.
Customizable Sensitivity: The sensitivity of movement detection can be adjusted by modifying the threshold values in the script.


## Requirements

- Python 3.x
- OpenCV
- dlib
- Twilio

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/face-motion-detector.git
   cd face-motion-detector

## Install the required packages:

pip install -r requirements.txt

Download the dlib shape predictor model and place it in the project directory. You can get it from dlib's website.
Update the detector.py file with your Twilio account SID, auth token, and phone numbers.


## Usage
Run the script:
python detector.py

Press Esc to exit the program.













