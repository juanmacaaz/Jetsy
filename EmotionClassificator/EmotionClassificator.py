from fer import FER
import matplotlib.pyplot as plt


class EmotionClassificator:
    def __init__(self):
        self.emo_detector = FER(mtcnn=True)
        self.emociones = {"angry": "enfadado", "disgust": "disgustado", "fear": "asustado", "happy": "feliz",
                          "sad": "triste", "surprise": "sorprendido", "neutral": "neutral"}

    def classificar(self, img):
        captured_emotions = self.emo_detector.detect_emotions(img)
        dominant_emotion, emotion_score = self.emo_detector.top_emotion(img)
        frase = "Escaneando resultados. Te ves " + self.emociones[dominant_emotion]
        return frase
