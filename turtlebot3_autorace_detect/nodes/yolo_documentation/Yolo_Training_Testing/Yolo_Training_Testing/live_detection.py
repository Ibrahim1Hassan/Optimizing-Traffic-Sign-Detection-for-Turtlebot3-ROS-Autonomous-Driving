from ultralytics import YOLO
import os

#Save pre-trained model in working directory of the code
# Load a model
model_path = os.path.join('.', 'runs', 'detect', 'train', 'weights', 'best.pt',)

model = YOLO(model_path)  # load pre-trained model

model(source="0", show=True, conf = 0.80) # Use pre-trained model with Webcam, if your webcam is in different source then 0 use that(0 is default)