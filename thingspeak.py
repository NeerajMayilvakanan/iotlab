
import RPi.GPIO as GPIO
import time
import urllib2

myapi="BRZ67XW5506HDJY8"
baseurl = "https://api.thingspeak.com/update?api_key=%s"%myapi

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
TRIG=23
ECHO=24
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG,False)
print('Waiting for sensor to settle')
time.sleep(0.0001)
start=0
end=0
while True:
    GPIO.output(TRIG,True)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        start=time.time()
    while GPIO.input(ECHO)==1:
        end=time.time()
        
    duration=end-start
    distance=duration*17150
    distance=round(distance,2)
    conn = urllib2.urlopen(baseurl+'&field1=%f' %(distance))
    conn.close()
    print('Distance'+str(distance))
    time.sleep(1)    
GPIO.cleanup()

        
      

    
