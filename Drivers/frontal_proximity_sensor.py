import RPi.GPIO as GPIO
import time

sensor = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
detect_object = True

while True:
    detect_object = GPIO.input(sensor)
    if not (detect_object):
        print("1")
        detect_object = True
    else:
        print("0")

    time.sleep(0.5)

