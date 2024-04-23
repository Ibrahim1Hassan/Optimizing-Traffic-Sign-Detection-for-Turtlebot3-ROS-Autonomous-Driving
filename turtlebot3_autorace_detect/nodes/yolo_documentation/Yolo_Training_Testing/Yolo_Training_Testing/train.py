from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # build a new model from scratch

# Use the model
results = model.train(data="config.yaml", epochs=65)  # train the model