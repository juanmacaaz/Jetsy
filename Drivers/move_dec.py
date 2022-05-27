import RPi.GPIO as GPIO
import time

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



while True:
	go()
	time.sleep(5)
	back()
	time.sleep(5)

	