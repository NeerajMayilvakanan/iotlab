import time
import RPi.GPIO as GPIO
import sys
import urllib2
#from LED_display import display_number
print('Measuring the distanceY')


print('reading the sensor data')
GPIO.setmode(GPIO.BCM)
trig = 2  # sends the signal
echo = 3  # listens for the signal
GPIO.setwarnings(False)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.output(trig, False)
print("Waiting for nSensor to settle")
time.sleep(2)
while True:
        GPIO.output(trig,True)
        time.sleep(1)
        GPIO.output(trig,False)
        while GPIO.input(echo) == 0:
                start = time.time()  # reached when echo listens
        while GPIO.input(echo) == 1:
                end = time.time() # reached when signal arrived
        distance = ((end - start) * 34300) / 2
        print(distance)
        print ('starting...')
        baseURL = 'https://api.thingspeak.com/update?api_key=PFQ00LPE92VM6G40' 
        while True:
                try:
                        print('entering try block')
                        f = urllib2.urlopen(baseURL + "&field1=%s" % int(distance/5))
                        print (f.read())
                        f.close()
                        sleep(15)
                except:
                        print( 'exiting.')
                        break
 
