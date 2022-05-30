import RPi.GPIO as GPIO
import time

pin1, pin2, pin3 = 32, 38, 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)

def animation0():
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.LOW)
    GPIO.output(pin3, GPIO.LOW)

def animation1():
    GPIO.output(pin1, GPIO.HIGH)
    GPIO.output(pin2, GPIO.LOW)
    GPIO.output(pin3, GPIO.LOW)

def animation2():
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.HIGH)
    GPIO.output(pin3, GPIO.LOW)

def animation3():
    GPIO.output(pin1, GPIO.HIGH)
    GPIO.output(pin2, GPIO.HIGH)
    GPIO.output(pin3, GPIO.LOW)

def animation4():
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.LOW)
    GPIO.output(pin3, GPIO.HIGH)

def animation5():
    GPIO.output(pin1, GPIO.HIGH)
    GPIO.output(pin2, GPIO.LOW)
    GPIO.output(pin3, GPIO.HIGH)

def animation6():
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.HIGH)
    GPIO.output(pin3, GPIO.HIGH)

while True:
    animation0()
    time.sleep(6)
    animation1()
    time.sleep(6)
    animation2()
    time.sleep(6)
    animation3()
    time.sleep(6)
    animation4()
    time.sleep(6)
    animation5()
    time.sleep(6)
    animation6()
    time.sleep(6)
