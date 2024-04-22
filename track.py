from ultralytics import YOLO

# Load an official or custom model
model = YOLO('/home/ubuntu/yolo/ultralytics-main/goldfish.pt')  # Load a custom trained model

# Perform tracking with the model
results = model.track(source="/home/ubuntu/yolo/ultralytics-main/datasets/g2.mp4", save=True, tracker="bytetrack.yaml")  # Tracking with ByteTrack tracker