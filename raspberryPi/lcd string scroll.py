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


def enable():  #to generate pulse
	GPIO.output(en,1)
	time.sleep(0.05)
	GPIO.output(en,0)
	time.sleep(0.05)

def lcd_cmd(x):
	# for MSB
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
	# for LSB
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
	length = len(x)
	for i in range(0,length):
		lcd_data(ord(x[i]))

while 1:
	init()
	lcd_cmd(0x80)
	strg_data("Loginware")
	time.sleep(0.5)
	while 1:
		lcd_cmd(0x1C)
