from ObjectClassificator.ObjectDetector import ObjectDetector
from ObjectClassificator.facedetection import detect_face
import cv2

def process_video(global_state):

    object_detector = ObjectDetector()
    cap = cv2.VideoCapture(0)

    while 1:
        ret, frame = cap.read()
        global_state['video'] = object_detector.image_classification(frame)
        global_state['face'] = detect_face(frame)