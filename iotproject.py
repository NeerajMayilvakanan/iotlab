import RPi.GPIO as GPIO
import subprocess
import time
import sys
import urllib2
import requests as r

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG=2
ECHO=3
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

TRIG1=14
ECHO1=15
GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)

TRIG2=5
ECHO2=6
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)

TRIG3=20
ECHO3=21
GPIO.setup(TRIG3,GPIO.OUT)
GPIO.setup(ECHO3,GPIO.IN)

GPIO.setup(17,GPIO.OUT)
GPIO.output(TRIG,False)
GPIO.output(TRIG1,False)
GPIO.output(TRIG2,False)
GPIO.output(TRIG3,False)

pulse_end = 0
pulse_end1=0
pulse_end2=0
pulse_end3=0
print "waiting for sensor to settle.."
time.sleep(2)
while(True):
	GPIO.output(TRIG,True)
	GPIO.output(TRIG1,True)
	GPIO.output(TRIG2,True)
	GPIO.output(TRIG3,True)
	time.sleep(0.0001)
	GPIO.output(TRIG,False)
	GPIO.output(TRIG1,False)
	GPIO.output(TRIG2,False)
	GPIO.output(TRIG3,False)
	
	print "........"
	while  GPIO.input(ECHO)==0:
		pulse_start=time.time()
	while GPIO.input(ECHO1)==0:
		pulse_start1=time.time()
	while  GPIO.input(ECHO2)==0:
		pulse_start2=time.time()
	while  GPIO.input(ECHO3)==0:
		pulse_start3=time.time()
	while GPIO.input(ECHO)==1:
		pulse_end=time.time()
	while  GPIO.input(ECHO1)==1:
		pulse_end1=time.time()
	if GPIO.input(ECHO2)==1:
		pulse_end2=time.time()
	if GPIO.input(ECHO3)==1:
		pulse_end3=time.time()
	
	print "............"		
	pulse_duration=pulse_end - pulse_start
	pulse_duration1=pulse_end1 - pulse_start1
	pulse_duration2=pulse_end2 - pulse_start2
	pulse_duration3=pulse_end3 - pulse_start3
	
	distance=pulse_duration*17150
	distance=round(distance,2)
	print "Distance1:",distance,"cm"
	distance1=pulse_duration1*17150
	distance1=round(distance1,2)
	print "Distance2:",distance1,"cm"
	distance2=pulse_duration2*17150
	distance2=round(distance2,2)
	print "Distance3:",distance2,"cm"
	distance3=pulse_duration3*17150
	distance3=round(distance3,2)
	print "Distance4:",distance3,"cm"

	baseURL='https://api.thingspeak.com//update?api_key=4HKR9EXWGO72F3LX'
	f=urllib2.urlopen(baseURL + "&field1=%s" % int(distance))
	baseURL='https://api.thingspeak.com//update?api_key=FDTP19Y4SA1ALINT'
	f=urllib2.urlopen(baseURL + "&field1=%s" % int(distance1))
	baseURL='https://api.thingspeak.com//update?api_key=OGBPXDNFX9B09UX14'
	f=urllib2.urlopen(baseURL + "&field1=%s" % int(distance2))
	baseURL='https://api.thingspeak.com//update?api_key=KGZT1401J384II2B'
	f=urllib2.urlopen(baseURL + "&field1=%s" % int(distance3))
	
	if(distance<5):
		GPIO.output(17,True)
		time.sleep(2)
		c=1
		di="IN NORTH"
	if(distance1<5):
		GPIO.output(17,True)
		time.sleep(2)
		c=1
		di="IN EAST"
	if(distance2<5):
		GPIO.output(17,True)
		time.sleep(2)
		c=1
		di="IN SOUTH"
	if(distance3<5):
		GPIO.output(17,True)
		time.sleep(2)
		c=1
		di="IN WEST"
		
	if(c==1):
		s="SOME KIND OF MOTION DETECTED "
		a1="....BE ALERT"
		r.get("http://smartmanoj.pythonanywhere.com/way2?u=8870586860&p=Paramsree&r=9750351051&t="+s+d1+a1)
		#print(r.status)
GPIO.cleanup()	
	

