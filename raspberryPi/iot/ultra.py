from ubidots import ApiClient 
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
trig=16
echo=18
R=29
G=31
B=33
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.setup(R,GPIO.OUT)
GPIO.setup(G,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)
api=ApiClient(token="BBFF-OHSRRigalIWGRTrTLtYTYxjNCP8v32")
var=api.get_variable('64ed921678f7bc000d81288a')
while 1:
	GPIO.output(trig,1)
	time.sleep(0.05)
	GPIO.output(trig,0)

	while(GPIO.input(echo)==0):
		start_time = time.time()
	while(GPIO.input(echo)==1):
		stop_time = time.time()

	duration = stop_time - start_time
	d = (duration *34300)/2
	if(d>10):
		GPIO.output(R,1)
		GPIO.output(G,0)
		GPIO.output(B,1)
	elif(d<10 and d>5):
		GPIO.output(R,1)
		GPIO.output(G,1)
		GPIO.output(B,0)
	elif(d<5):
		GPIO.output(R,0)
		GPIO.output(G,1)
		GPIO.output(B,1)
	print(round(d,2),"cm")
	response=var.save_value({"value":d})
	time.sleep(1)
	#return d
