import cv2
import numpy as np
import matplotlib.pyplot as plt

NOMBRE = 'corazon'
cap = cv2.VideoCapture(f'{NOMBRE}.mp4')

WINDOW_SIZE = 10

old_frame = np.zeros((24, 32), dtype=np.uint8)

datos = []
lista_numero_cambios = []
n_frames = 0

while(cap.isOpened()):
    numero_cambios = 0
    ret, frame = cap.read()

    if ret == True:

        frame[frame > 127] = 255
        frame[frame <= 127] = 0

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(frame, (32, 24), interpolation = cv2.INTER_AREA)

        resized[resized > 10] = 255
        resized[resized <= 10] = 0

        # Codigo aqui


        for i in range(24):
            for j in range(32):
                if old_frame[i, j] != resized[i, j]:
                    numero_cambios += 1
                    datos.append((i, j, resized[i, j]))

        # Generar codigo array

        old_frame = resized
        n_frames+=1
        lista_numero_cambios.append(numero_cambios)

    else:
        break

for _ in range(100):
    datos.append((0,0,0))

size = len(lista_numero_cambios) + 1 + (len(datos) * 3)

output = "unsigned char " + NOMBRE + "["+str(size)+"] = { "
output += str(n_frames) + ", "
for i in lista_numero_cambios:
    output += str(i) + ", "
for i in datos:
    output += str(i[0]) + ", " + str(i[1]) + ", " + str(i[2]) + ", "

output = output[:-2]
output += "};"

print(output)