import RPi.GPIO as GPIO
import time
in1=13
in2=15
sw=7
R=3
G=5
B=11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(R,GPIO.OUT)
GPIO.setup(G,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)
GPIO.setup(sw,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
cnt=0
while 1:
        val=GPIO.input(sw)
        time.sleep(0.2)
        if not val and cnt==0:
                GPIO.output(in1,1)
                GPIO.output(in2,0)
                GPIO.output(R,1)
                GPIO.output(G,0)
                GPIO.output(B,1)
                cnt=cnt+1
        elif not val and cnt==1:
                GPIO.output(in1,0)
                GPIO.output(in2,1)
                GPIO.output(R,1)
                GPIO.output(G,1)
                GPIO.output(B,0)
                cnt=cnt+1
        elif not val and cnt==2:
                GPIO.output(in1,0)
                GPIO.output(in2,0)
                GPIO.output(R,0)
                GPIO.output(G,1)
                GPIO.output(B,1)
                cnt=0
