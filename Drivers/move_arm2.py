import RPi.GPIO as GPIO
import time

pin1, pin2 = 7, 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

def state0():
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.LOW)

def state1():
    GPIO.output(pin1, GPIO.HIGH)
    GPIO.output(pin2, GPIO.LOW)

def state2():
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.HIGH)

def state3():
    GPIO.output(pin1, GPIO.HIGH)
    GPIO.output(pin2, GPIO.HIGH)

while True:
    state0()
    time.sleep(6)
    state1()
    time.sleep(6)
    state2()
    time.sleep(6)
    state3()
    time.sleep(6)
