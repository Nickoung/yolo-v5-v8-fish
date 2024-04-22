from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n-seg.pt')  # load an official model
model = YOLO('/home/ubuntu/yolo/ultralytics-main/runs/segment/train/weights/best.pt')  # load a custom model

# Predict with the model
results = model(source='/home/ubuntu/yolo/ultralytics-main/datasets/fishseg/fishseg-test',save=True)  # predict on an image