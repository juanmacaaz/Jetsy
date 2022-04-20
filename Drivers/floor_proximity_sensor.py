import RPi.GPIO as GPIO
import time

sensor = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
detect_object = True
 
while True:
    detect_object = GPIO.input(sensor)
    if (detect_object):
        print("No floor")
        detect_object = True
        time.sleep(0.5)
