import cv2
import numpy as np


def image_classification(model_weights, model_architecture, image):
    blob = cv2.dnn.blobFromImage(image, 0.017, (224, 224), (103.94, 116.78, 123.68))
    global model, classes
    rows = open('synset_words.txt').read().strip().split("\n")
    image_classes = [r[r.find(" ") + 1:].split(",")[0] for r in rows]
    model = cv2.dnn.readNetFromCaffe(model_architecture, model_weights)
    model.setInput(blob)
    output = model.forward()
    new_output = output.reshape(len(output[0][:]))
    expanded = np.exp(new_output - np.max(new_output))
    prob = expanded / expanded.sum()
    conf = np.max(prob)
    index = np.argmax(prob)
    label = image_classes[index]
    return label, conf


model_architecture = 'DenseNet_121.prototxt'
model_weights = 'DenseNet_121.caffemodel'
image1 = cv2.imread('gato.jfif')
label, conf = image_classification(model_weights, model_architecture, image1)
print(label, conf)
