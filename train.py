from ultralytics import YOLO

# Load a model
model = YOLO('/home/ubuntu/yolo/ultralytics-main/ultralytics/cfg/models/v8/insects.yaml')  # build a new model from YAML
model = YOLO('/home/ubuntu/yolo/ultralytics-main/yolov8n.pt')  # load a pretrained model (recommended for training)
model = YOLO('/home/ubuntu/yolo/ultralytics-main/ultralytics/cfg/models/v8/insects.yaml').load('/home/ubuntu/yolo/ultralytics-main/yolov8n.pt')  # build from YAML and transfer weights

# Train the model
results = model.train(data='/home/ubuntu/yolo/ultralytics-main/ultralytics/cfg/datasets/insects.yaml', epochs=100)


