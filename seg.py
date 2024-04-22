from ultralytics import YOLO

# Load a model
model = YOLO('/home/ubuntu/yolo/ultralytics-main/ultralytics/cfg/models/v8/fishseg.yaml')  # build a new model from YAML
model = YOLO('/home/ubuntu/yolo/ultralytics-main/yolov8n-seg.pt')  # load a pretrained model (recommended for training)
model = YOLO('/home/ubuntu/yolo/ultralytics-main/ultralytics/cfg/models/v8/fishseg.yaml').load('/home/ubuntu/yolo/ultralytics-main/yolov8n.pt')  # build from YAML and transfer weights

# Train the model
results = model.train(data='/home/ubuntu/yolo/ultralytics-main/ultralytics/cfg/datasets/fishseg.yaml', epochs=50)