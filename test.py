from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")

results = model.val(
    data="Fire-Detection/data.yaml",  # senin yaml yolu
    imgsz=640,
    conf=0.25,
    iou=0.5,
    device="mps"  # ya da "cpu"
)

print(results)
print("mAP50:", results.box.map50)
print("mAP50-95:", results.box.map)
print("Precision:", results.box.mp)
print("Recall:", results.box.mr)


