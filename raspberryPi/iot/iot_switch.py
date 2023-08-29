from ubidots import ApiClient
import RPi.GPIO as GPIO
import time
led=3
led1=5
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(led1,GPIO.OUT)
api=ApiClient(token="BBFF-OHSRRigalIWGRTrTLtYTYxjNCP8v32")
var=api.get_variable('64ed78cb78f7bc000bcc70a7')
val=api.get_variable('64ed8760eb9ba9000d5f0256')
while 1:
	var1=var.get_values(1)
	val1=val.get_values(1)
	d=var1[0]['value']
	s=val1[0]['value']
	if(d==1):
		GPIO.output(led,1)
		print('on')
	elif(d==0):
		GPIO.output(led,0)
		print('off')
	if(s==1):
		GPIO.output(led1,1)
		print('on')
	elif(s==0):
		GPIO.output(led1,0)
		print('off')

