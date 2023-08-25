import Adafruit_DHT
import RPi.GPIO as GPIO
import time

def hum_temp():
	hum,temp=Adafruit_DHT.read_retry(11,4)
	#print(hum)
	#print(temp)
	str1 = f"H:{hum} T:{temp}"
	return str1
