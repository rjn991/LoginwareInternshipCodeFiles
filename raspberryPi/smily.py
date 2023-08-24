import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
rs=3
en=5
d4=40
d5=38
d6=36
d7=35

GPIO.setup(rs,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.setup(d4,GPIO.OUT)
GPIO.setup(d5,GPIO.OUT)
GPIO.setup(d6,GPIO.OUT)
GPIO.setup(d7,GPIO.OUT)

def enable():
	GPIO.output(en,1)
	time.sleep(0.0005)
	GPIO.output(en,0)
	time.sleep(0.0005)

def lcd_cmd(x):
	#For MSB
	GPIO.output(rs,0)
	GPIO.output(d4,0)
	GPIO.output(d5,0)
	GPIO.output(d6,0)
	GPIO.output(d7,0)
	if x & 0x10==0x10:
		GPIO.output(d4,1)
	if x & 0x20==0x20:
		GPIO.output(d5,1)
	if x & 0x40==0x40:
		GPIO.output(d6,1)
	if x & 0x80==0x80:
		GPIO.output(d7,1)
	enable()

	#For LSB
	GPIO.output(d4,0)
	GPIO.output(d5,0)
	GPIO.output(d6,0)
	GPIO.output(d7,0)
	if x & 0x01==0x01:
		GPIO.output(d4,1)
	if x & 0x02==0x02:
		GPIO.output(d5,1)
	if x & 0x04==0x04:
		GPIO.output(d6,1)
	if x & 0x08==0x08:
		GPIO.output(d7,1)
	enable()

def lcd_data(x):
	#For MSB bit 
	GPIO.output(rs,1)
	GPIO.output(d4,0)
	GPIO.output(d5,0)
	GPIO.output(d6,0)
	GPIO.output(d7,0)
	if x & 0x10==0x10:
		GPIO.output(d4,1)
	if x & 0x20==0x20:
		GPIO.output(d5,1)
	if x & 0x40==0x40:
		GPIO.output(d6,1)
	if x & 0x80==0x80:
		GPIO.output(d7,1)
	enable()

	#For LSB bit
	GPIO.output(d4,0)
	GPIO.output(d5,0)
	GPIO.output(d6,0)
	GPIO.output(d7,0)
	if x & 0x01==0x01:
		GPIO.output(d4,1)
	if x & 0x02==0x02:
		GPIO.output(d5,1)
	if x & 0x04==0x04:
		GPIO.output(d6,1)
	if x & 0x08==0x08:
		GPIO.output(d7,1)
	enable()

def init():
	lcd_cmd(0x33)
	lcd_cmd(0x32)
	lcd_cmd(0x28)
	lcd_cmd(0x0c)
	lcd_cmd(0x0e)
	lcd_cmd(0x01)

def strg_data(x):
	length=len(x)
	for i in range(0,length):
		lcd_data(ord(x[i]))

def custom():
	lcd_cmd(64)
	lcd_data(14)
	lcd_data(10)
	lcd_data(27)
	lcd_data(17)
	lcd_data(17)
	lcd_data(17)
	lcd_data(17)
	lcd_data(31)
	lcd_cmd(0x80)
	lcd_data(0)
	time.sleep(1)

	lcd_cmd(64)
	lcd_data(14)
	lcd_data(10)
	lcd_data(27)
	lcd_data(17)
	lcd_data(17)
	lcd_data(17)
	lcd_data(31)
	lcd_data(31)
	lcd_cmd(0x80)
	lcd_data(0)
	time.sleep(1)
	
	lcd_cmd(64)
	lcd_data(14)
	lcd_data(10)
	lcd_data(27)
	lcd_data(17)
	lcd_data(17)
	lcd_data(31)
	lcd_data(31)
	lcd_data(31)
	lcd_cmd(0x80)
	lcd_data(0)
	time.sleep(1)

	lcd_cmd(64)
	lcd_data(14)
	lcd_data(10)
	lcd_data(27)
	lcd_data(17)
	lcd_data(31)
	lcd_data(31)
	lcd_data(31)
	lcd_data(31)
	lcd_cmd(0x80)
	lcd_data(0)
	time.sleep(1)

	lcd_cmd(64)
	lcd_data(14)
	lcd_data(10)
	lcd_data(27)
	lcd_data(31)
	lcd_data(31)
	lcd_data(31)
	lcd_data(31)
	lcd_data(31)
	lcd_cmd(0x80)
	lcd_data(0)
	time.sleep(1)

	lcd_cmd(64)
	lcd_data(14)
	lcd_data(14)
	lcd_data(31)
	lcd_data(31)
	lcd_data(31)
	lcd_data(31)
	lcd_data(31)
	lcd_data(31)
	lcd_cmd(0x80)
	lcd_data(0)
	time.sleep(1)

def smily():
	lcd_cmd(72)
	lcd_data(0)
	lcd_data(10)
	lcd_data(0)
	lcd_data(4)
	lcd_data(17)
	lcd_data(14)
	lcd_data(0)
	lcd_data(0)
	lcd_cmd(0x81)
	lcd_data(1)
	time.sleep(1)


while 1:
	init()
	custom()
	#lcd_cmd(0x80)
	#strg_data("hi")
	smily()
