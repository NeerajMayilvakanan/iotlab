import RPi.GPIO as GPIO
import subprocess
import time
GPIO.cleanup()
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
	time.sleep(1)
	GPIO.output(TRIG, False)
	while GPIO.input(ECHO)==0:
		pulse_start = time.time()
		
	while GPIO.input(ECHO)==1:
		pulse_end = time.time()
	
	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration*17150
	distance = round(distance, 2)
	print ("Distance:",distance,"cm")
	time.sleep(1)
	
	
GPIO.cleanup()

