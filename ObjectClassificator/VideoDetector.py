from ObjectClassificator.ObjectDetector import ObjectDetector
from ObjectClassificator.facedetection import detect_face
from ObjectClassificator.EmotionClassificator import EmotionClassificator
import cv2

def process_video(global_state):

    object_detector = ObjectDetector()
    emotion_classificator = EmotionClassificator()
    cap = cv2.VideoCapture(0)

    while 1:
        ret, frame = cap.read()
        global_state['video'] = object_detector.image_classification(frame)
       
        result = emotion_classificator.classificar(frame)
        global_state['face'] = result[0]
        global_state["emotion"] = result[1]