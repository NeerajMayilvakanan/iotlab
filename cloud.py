import time
# import RPi.GPIO as GPIO
import sys
import urllib3
#from LED_display import display_number
print('Measuring the distanceY')
print('reading the sensor data')
# GPIO.setmode(GPIO.BCM)


trig = 2  # sends the signal
echo = 3  # listens for the signal
# GPIO.setwarnings(False)

# GPIO.setup(trig, GPIO.OUT)
# GPIO.setup(echo, GPIO.IN)
# GPIO.output(trig, False)
print("Waiting for sensor to settle")
time.sleep(2)
while True:
  # GPIO.output(trig, True)
  time.sleep(1)
  # GPIO.output(trig, False)
  # while (GPIO.input(echo)==0):
    # start=time.time()/
  # while (GPIO.input(echo)==1):
    # end=time.time()
  # distance = ((end-start)*34300)/2
  # print(distance)
  print ('starting...')
  baseURL = 'https://api.thingspeak.com/update?api_key=Y6W0C019QF8STBMQ' 
  a=23456
  while True:
          try:
                  print('entering try block')
                  f = urllib3.urlopen(baseURL + "&field1=%s" % int(a/5))
                  a=a+123
                  print (f.read())
                  f.close()
                  time.sleep(15)
          except:
                  print("quitting...")
                  break

