from ubidots import ApiClient 
import RPi.GPIO as GPIO
R=3
G=5
B=11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(R,GPIO.OUT)
GPIO.setup(G,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)
api=ApiClient(token="BBFF-OHSRRigalIWGRTrTLtYTYxjNCP8v32")
var=api.get_variable('64eed455861634000b3a9d90')
while 1:
	var1=var.get_values(1)
	d=var1[0]['value']
	d=int(d)
	print(d)
	if d==0:
		GPIO.output(R,0)
		GPIO.output(G,1)
		GPIO.output(B,1)
	elif d==1:
		GPIO.output(R,1)
		GPIO.output(G,0)
		GPIO.output(B,1)
	elif d==2:
		GPIO.output(R,1)
		GPIO.output(G,1)
		GPIO.output(B,0)
	elif d==3:
		GPIO.output(R,1)
		GPIO.output(G,1)
		GPIO.output(B,1)


