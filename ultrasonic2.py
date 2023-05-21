import RPi.GPIO as GPIO
import subprocess
import time
GPIO.setmode(GPIO.BCM)
TRIG = 2
ECHO = 3
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
time.sleep(2)
f=open('test.txt','w')
while(True):
        GPIO.output(TRIG, True)
        time.sleep(1)
        GPIO.output(TRIG, False)
        while GPIO.input(ECHO)==0:
                pulse_starte = time.time()
        while GPIO.input(ECHO)==1:
                pulse_end = time.time()
            
        pulse_duration = pulse_end - pulse_starte

        distance = pulse_duration*17150
        distance = round(distance, 2)
        print "Distance:",distance,"cm"
        distance="distance"+ " - " +str(distance)
        f=open('test.txt','a')
        f.write(str(distance))
        f.write('\n')

f.close()   
GPIO.cleanup()

