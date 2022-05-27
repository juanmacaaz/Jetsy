import cv2
import numpy as np


class ObjectDetector:
    def __init__(self):
        self.model_architecture = 'ObjectClassificator/DenseNet_121.prototxt'
        self.model_weights = 'ObjectClassificator/DenseNet_121.caffemodel'
        self.model = cv2.dnn.readNetFromCaffe(self.model_architecture, self.model_weights)
        rows = open('ObjectClassificator/synset_words.txt').read().strip().split("\n")
        self.image_classes = [r[r.find(" ") + 1:].split(",")[0] for r in rows]

    def image_classification(self, image):
        blob = cv2.dnn.blobFromImage(image, 0.017, (224, 224), (103.94, 116.78, 123.68))
        self.model.setInput(blob)
        output = self.model.forward()
        new_output = output.reshape(len(output[0][:]))
        expanded = np.exp(new_output - np.max(new_output))
        prob = expanded / expanded.sum()
        conf = np.max(prob)
        index = np.argmax(prob)
        label = self.image_classes[index]
        return label, conf

