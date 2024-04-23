Main content of directory modified or added:
        1 config.yaml: it is configuration file of custom dataset used
        2 detect_sign.py: it is the node used for detection of signs using YOLO+SIFT
        3 images: it contains images which are trained for model
        4 labels: annotations of the same images which are used for model
        5 live_detection.py: it to use prre-trained model for traffic sign detection through webcam of laptop
        6 requirements.txt: libraries required to be installed for using YOLO
        7 runs: contains pre-trained models
        8 train.py: node to train the images with annotation and make a model
        9 yolov8.pt: used in train.py as reference for training model

To use pre-trained model

Step 1: install requirememts.txt

Step 2: Once requirements are fulfilled copy "runs"(It contains pre_trained model) folder and paste it in the working directory of the code
        In case of "detect_sign" node place in .ros (Hidden Folder in Home Directory)
        In case of "live_detection" node place it in the working directory (in "turtlebot3_Autorace_detect/nodes")

Step 3: Replace existing "detect_sign" node with "detect_sign" node provided

Step 4: Check model_path in both "detect_sign" and "live_detection"

Step 5: Run "live_detection.py" for traffic sign recognition through Webcam (If you are using Vitiual Machine make sure to give permission to use Webcam from devices before running code)
        Run "detect_sign" node normally and it will directly detect with YOLO


To train your own model

Step 1: install requirements.txt

Step 2: Take images of object/sign you want to detect with different background

Step 3: Do annotation of each image (I have used cvat.ai online tool for that)

Step 4: Once you annoted images if you have used online tool then export dataset 

Step 5: Create two seprate directories in the same directory you have "train.py" file
        Directory 1 : images (copy all images you have annotated in this directory)
        Directory 2: labels (copy all labels you have got from dataset you exported in this directory)

Step 6: Modify config.yaml file 
        classes: as per labels of your annotation (Do not change the order keep same order of classes as labels)
        path: change as per your working directory in which you have placed "train.py" and "images" 

Step 7: Run "train.py" file (set epochs as per your requirements)

Step 8: Once training is completed you can find a "runs" directory in your working directory. This contains report of the training and weights of your trained model.