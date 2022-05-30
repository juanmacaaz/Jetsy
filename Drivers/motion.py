from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
import time

myKit = ServoKit(channels=16)

# BRAZOS
pinA, pinB = 7, 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinA, GPIO.OUT)
GPIO.setup(pinB, GPIO.OUT)

def state0():
    GPIO.output(pinA, GPIO.LOW)
    GPIO.output(pinB, GPIO.LOW)

def state1():
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.LOW)

def state2():
    GPIO.output(pinA, GPIO.LOW)
    GPIO.output(pinB, GPIO.HIGH)

def state3():
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.HIGH)

# MOTORES DC

A1A = 35
A1B = 36

A2A = 37
A2B = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setup(A1A, GPIO.OUT)
GPIO.setup(A1B, GPIO.OUT)
GPIO.setup(A2A, GPIO.OUT)
GPIO.setup(A2B, GPIO.OUT)


def go():
    GPIO.output(A1A, GPIO.LOW)
    GPIO.output(A1B, GPIO.HIGH)

    GPIO.output(A2A, GPIO.LOW)
    GPIO.output(A2B, GPIO.HIGH)

def back():
    GPIO.output(A1A, GPIO.HIGH)
    GPIO.output(A1B, GPIO.LOW)
	
    GPIO.output(A2A, GPIO.HIGH)
    GPIO.output(A2B, GPIO.LOW)

def girar_derecha():
    GPIO.output(A1A, GPIO.HIGH)
    GPIO.output(A1B, GPIO.LOW)
	
    GPIO.output(A2A, GPIO.LOW)
    GPIO.output(A2B, GPIO.HIGH)

def girar_izquierda():
    GPIO.output(A1A, GPIO.LOW)
    GPIO.output(A1B, GPIO.HIGH)
	
    GPIO.output(A2A, GPIO.HIGH)
    GPIO.output(A2B, GPIO.LOW)

# SENSORES CAIDA
sensor_left = 13
sensor_right = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor_left, GPIO.IN)
GPIO.setup(sensor_right, GPIO.IN)

def detectar_caida():
    detect_object_left = GPIO.input(sensor_left)
    detect_object_right = GPIO.input(sensor_right)

    if (detect_object_left or detect_object_right):
        return True
    else: 
        return False

# ANIMACIONES

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

# SENSOR FRONTAL
frontal_sensor = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(frontal_sensor,GPIO.IN)
def detector_frontal():
    detect_object = GPIO.input(frontal_sensor)
    if not (detect_object):
        return False
    else:
        return True
