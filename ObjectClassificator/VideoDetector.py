#from ObjectClassificator.ObjectDetector import ObjectDetector
#from ObjectClassificator.facedetection import detect_face
#from ObjectClassificator.EmotionClassificator import EmotionClassificator
#import cv2

import time

# DEMO RECONOCER OBJETOS

objeto = [('glass', 90)]
face = ['False']
emotion = ['neutral']

def process_video(global_state):

    #object_detector = ObjectDetector()
    #emotion_classificator = EmotionClassificator()
    #cap = cv2.VideoCapture(0)

    indice = 0

    while 1:
        #ret, frame = cap.read()
        global_state['video'] = objeto[indice]#object_detector.image_classification(frame)
       
        #result = emotion_classificator.classificar(frame)
        global_state['face'] = face[indice]#result[0]
        global_state["emotion"] = emotion[indice]#result[1]
        indice += 1 % len(objeto)
        time.sleep(0.5)
