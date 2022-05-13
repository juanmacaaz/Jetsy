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
        frase = "Escaneando resultados. Te ves " + str(self.emociones[dominant_emotion])
        return frase


img = cv2.imread("juan.png")
a = EmotionClassificator()
print(a.classificar(img))

