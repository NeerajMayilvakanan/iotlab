import RPi.GPIO as GPIO
import subprocess
import time
GPIO.setmode(GPIO.BCM)
TRIG = 2
ECHO = 3
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(3,GPIO.OUT)
GPIO.output(TRIG, False)
print ("Waiting For Sensor To Settle")
time.sleep(2)

while(True):
	GPIO.output(TRIG, True)
	GPIO.output(TRIG, False)
	while GPIO.input(ECHO)==0:
		pulse_start = time.time()
	while GPIO.input(ECHO)==1:
		pulse_end = time.time()
	
	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration*17150
	distance = round(distance, 2)
	if(distance>30)
            GPIO.output(3,True)
        else
            GPIO.output(3,False)
	print ("Distance:",distance,"cm")
	
	
GPIO.cleanup()

