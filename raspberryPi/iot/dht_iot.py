from ubidots import ApiClient
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
api=ApiClient(token="BBFF-5OuCxY9nf2aQcZq385s3U4XqZo58DW")
t=api.get_variable('64eec6ca288a93000c120757')
h=api.get_variable('64eec6d10788ec000d745051')
while 1:
	hum,temp=Adafruit_DHT.read_retry(11,4) #11 is the  version amd 4 is gpio4=pin 7
	print(hum)
	print(temp)
	t.save_value({"value":temp})
	h.save_value({"value":hum})
