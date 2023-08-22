import RPi.GPIO as GPIO
import time
sw=13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sw,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while 1:
	val=GPIO.input(sw)
	print ("Push btn value:", val)
