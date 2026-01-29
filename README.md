# Fire Detection with YOLOv8 

This project implements a custom fire detection system using a YOLOv8 object detection model trained on a fire dataset and deployed with OpenCV for image, video, and real-time inference.

The goal of this project is to demonstrate how deep learning–based object detection can be applied to early fire detection scenarios, such as surveillance systems, industrial safety, and smart monitoring applications.


<img width="176" height="206" alt="Ekran Resmi 2026-01-29 00 00 40" src="https://github.com/user-attachments/assets/d2d088a2-1d6e-4dad-b806-1856834b05da" />




---

## Features
- Custom-trained YOLOv8 fire detection model
- Single-class object detection (`fire`)
- Image, video (MP4), and webcam inference
- OpenCV-based visualization
- High detection accuracy on validation data

---

## Model Performance
Evaluated on the validation set:

- Precision: ~0.87  
- Recall: ~0.76  
- mAP@0.5: ~0.86  
- mAP@0.5:0.95: ~0.58  

These results indicate strong detection performance for a single-class fire detection task.

---

## Project Structure
```text
Fire-Detection-with-YOLOv8/
├─ Fire-Detection/
│  ├─ data.yaml
│  └─ test/images/
├─ main.py              # Training / evaluation entry
├─ predict_one.py       # Single image inference
├─ requirements.txt
└─ README.md
```
Installation
``` bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Notes
The confidence threshold can be adjusted to balance false positives and recall.
This project focuses on computer vision and applied AI, not real-world deployment or safety certification.
Author
Berke Tozkoparan
Industrial Engineering (English) | AI & Computer Vision
GitHub: https://github.com/BerkeTozkoparam
