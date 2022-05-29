from adafruit_servokit import ServoKit
import time

myKit = ServoKit(channels=16)
while True:
        myKit.servo[1].angle = 0
        myKit.servo[2].angle = 0
        time.sleep(1)
        myKit.servo[1].angle = 90
        myKit.servo[2].angle = 90
        time.sleep(1)
