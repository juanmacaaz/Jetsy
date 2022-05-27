from adafruit_servokit import ServoKit
<<<<<<< HEAD

myKit = ServoKit(channels=16)
myKit.servo[0].angle = 90
=======
import time

myKit = ServoKit(channels=16)
while True:
        myKit.servo[1].angle = 0
        myKit.servo[2].angle = 0
        time.sleep(1)
        myKit.servo[1].angle = 90
        myKit.servo[2].angle = 90
        time.sleep(1)
>>>>>>> 1db9c9920db1e0d6822e3f2742faf9e4bb2269e2
