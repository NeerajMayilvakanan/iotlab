import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
while True:
    GPIO.output(2,True)
   
    print("on")
    time.sleep(1)
    GPIO.output(2,False)
    print("off") 
    time.sleep(1)
    GPIO.output(3,True)
    
    
    print("on")
    time.sleep(1)
    GPIO.output(3,False)
    print("off") 
    time.sleep(1)
    GPIO.output(4,True)
   
    print("on")
    time.sleep(1)
    GPIO.output(4,False)
    print("off") 
    time.sleep(1)
GPIO.cleanup()
