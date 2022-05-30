from fer import FER
import matplotlib.pyplot as plt
import cv2

from ObjectClassificator.facedetection import detect_face

class EmotionClassificator:
    def __init__(self) -> None:
        self.emo_detector = FER(mtcnn=False)

    def classificar(self, img):
        faces = detect_face(img)
        if len(faces) < 1:
            return 0, None
        # Draw rectangle around the faces and crop the faces
        for (x, y, w, h) in faces:
            img = img[y:y + h, x:x + w]
        if img.shape[0] == 0 or img.shape[1] == 0:
            return 0, None
        dominant_emotion, emotion_score = self.emo_detector.top_emotion(img)
        if dominant_emotion is None:
            return 0, None
        return len(faces) >= 1 , dominant_emotion
    

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

