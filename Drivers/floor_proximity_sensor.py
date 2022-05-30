import RPi.GPIO as GPIO
import time

sensor_left = 13
sensor_right = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor_left, GPIO.IN)
GPIO.setup(sensor_right, GPIO.IN)

detect_object_left = True
detect_object_right = True

while True:
    detect_object_left = GPIO.input(sensor_left)
    detect_object_right = GPIO.input(sensor_right)

    if (detect_object_left and detect_object_right):
        print("3")
        detect_object_left = True
        detect_object_right = True

    elif (detect_object_left):
        print("2")
        detect_object_left = True

    elif (detect_object_right):
        print("1")
        detect_object_right = True 
    else:
        print("0")
    
    time.sleep(0.5)
