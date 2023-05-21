import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(2,GPIO.OUT)

GPIO.setup(3, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:

	if(GPIO.input(3) == 1):
		GPIO.output(2,True)
		time.sleep(1)
		print("LED ON")
	else:
		GPIO.output(2,False)
		time.sleep(1)
		print("LED OFF")

GPIO.cleanup()

