import RPi.GPIO as GPIO
import time 
R=3
G=5
B=11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(R,GPIO.OUT)
GPIO.setup(G,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)
for i in range(5):
	GPIO.output(R,0)
	GPIO.output(G,1)
	GPIO.output(B,1)
	time.sleep(1)
	GPIO.output(R,1)
	GPIO.output(G,1)
	GPIO.output(B,1)
	time.sleep(1)

