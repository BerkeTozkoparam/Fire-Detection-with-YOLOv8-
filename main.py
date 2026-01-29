import numpy as np
from  ultralytics import YOLO
#Model 
def main():
    model = YOLO("yolov8n.pt")
    model.train(
        data="/Users/berkebarantozkoparan/Desktop/proje5/Fire-Detection/data.yaml",
        epochs=50,
        imgsz=640,
        batch=8,
        device="mps"  # GPU varsa "0"
    )

if __name__ == "__main__":
    main()
