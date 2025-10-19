# 🃏 Poker Detection with YOLOv8

A small but fun computer vision project that uses **YOLOv8** to **detect poker cards** in real-time from a webcam.  
Built with **Python, OpenCV, and Ultralytics YOLO** — perfect for learning or demonstrating object detection on custom datasets.

## 🚀 Features
✅ Detects all 52 standard poker cards (suit + rank)  
✅ Displays card name and confidence score in real-time  
✅ Runs on both CPU and GPU (CUDA supported)  
✅ Easy to retrain or extend for other card types

## 🧩 Project Structure
Poker_detection_with_YOLOv8/ 
├── poker_rank.py # Poker hand ranking logic
├── test_webcam.py # Real-time detection using webcam
├── poker.pt # Trained YOLOv8 model
├── README.md # This file
└── LICENSE

## ⚙️ Installation

### 1: Clone the repository
git clone https://github.com/huynoob1312/Poker_detection_with_YOLOv8.git
cd Poker_detection_with_YOLOv8

### 2: install requirement library
pip install ultralytics opencv-python torch torchvision

### 3: run webcam
python .\detect.py

## 👨‍💻 Author
gmail: phamviethuy131225@gmail.com

## 🙏 Credits
This project was inspired by the amazing work of the [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) team.  
It also draws ideas from several open-source tutorials and community projects on real-time object detection.  

If you used any specific dataset (for example, a Roboflow dataset), you can add:
> Dataset: [Playing Cards Computer Vision Model – Roboflow](https://universe.roboflow.com/augmented-startups/playing-cards-ow27d)

Idea and implementation were based on the GitHub repository [github](https://github.com/TruongTanNghia/YOLOV8_Object-Detection) — which provided the initial concept for poker card detection.  

Special thanks to the open-source community for making AI development accessible and fun 🎴
