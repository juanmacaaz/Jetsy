from fer import FER
import matplotlib.pyplot as plt
import cv2

class EmotionClassificator:
    def __init__(self):
        self.emociones = {"angry": "enfadado", "disgust": "disgustado", "fear": "asustado", "happy": "feliz",
                          "sad": "triste", "surprise": "sorprendido", "neutral": "neutral"}

    def classificar(self, img):
        emo_detector = FER(mtcnn=True)
        captured_emotions = emo_detector.detect_emotions(img)
        dominant_emotion, emotion_score = emo_detector.top_emotion(img)
        if dominant_emotion is None:
            return None
        return self.emociones[dominant_emotion]
    

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    emociones = EmotionClassificator()
    while True:
        ret, frame = cap.read()
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        emocion = emociones.classificar(frame)
        print(emocion)
    cap.release()
    cv2.destroyAllWindows()

