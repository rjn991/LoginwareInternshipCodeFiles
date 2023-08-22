import RPi.GPIO as GPIO
import time
sw=7
R=3
GPIO.setmode(GPIO.BOARD)
GPIO.setup(R,GPIO.OUT)
GPIO.setup(sw,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while 1:
        val=GPIO.input(sw)
        if not val:
                GPIO.output(R,0)
        else:
                GPIO.output(R,1)

