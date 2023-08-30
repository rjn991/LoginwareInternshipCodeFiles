from ubidots import ApiClient 
import RPi.GPIO as GPIO
import telepot


token = '6387379359:AAEo9xEosNf3npjE-oGyzGGkljbZZkIdcm0' # telegram token
receiver_id=986893115  # https://api.telegram.org/bot<TOKEN>/getUpdates
bot = telepot.Bot(token)

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
		bot.sendMessage(receiver_id, 'Red On') 
	elif d==1:
		GPIO.output(R,1)
		GPIO.output(G,0)
		GPIO.output(B,1)
		bot.sendMessage(receiver_id, 'Green On') 
	elif d==2:
		GPIO.output(R,1)
		GPIO.output(G,1)
		GPIO.output(B,0)
		bot.sendMessage(receiver_id, 'Blue On') 
	elif d==3:
		GPIO.output(R,1)
		GPIO.output(G,1)
		GPIO.output(B,1)
		bot.sendMessage(receiver_id, 'LED Off') 


