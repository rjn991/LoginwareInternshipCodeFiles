import RPi.GPIO as GPIO
import time
in1=13
in2=15
GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
while 1:
        GPIO.output(in1,1)
        GPIO.output(in2,0)
        time.sleep(3)
        GPIO.output(in1,0)
        GPIO.output(in2,1)
        time.sleep(3)
        GPIO.output(in1,0)
        GPIO.output(in2,0)
        time.sleep(1)

