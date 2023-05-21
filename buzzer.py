import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(3,GPIO.OUT)

while True:

		GPIO.output(3,True)
		print("on")
		time.sleep(1)
		GPIO.output(3,False)
		print("off")
		time.sleep(3)

GPIO.cleanup()

