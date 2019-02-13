from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
detector.loadModel()


def ana(In):
        detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, "images\{}.jpg".format(In)), output_image_path=os.path.join(execution_path , "pImages\{}new.jpg".format(In)), minimum_percentage_probability=30)
        x = 0
        for eachObject in detections:
                if(str(eachObject["name"]) == 'person' and float(eachObject["percentage_probability"]) > 0.7):
                        x = x + 1
        return(x)