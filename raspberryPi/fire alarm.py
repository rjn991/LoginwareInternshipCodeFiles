import RPi.GPIO as GPIO
import time
fs=12
b=3
GPIO.setmode(GPIO.BOARD)
GPIO.setup(b,GPIO.OUT)
GPIO.setup(fs,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while 1:
        val=GPIO.input(fs)
        if not val:
                GPIO.output(b,1)
        else:
                GPIO.output(b,0)
