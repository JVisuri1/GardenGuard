import RPi.GPIO as GPIO
import time

class GroundMoistureSensor:
	def __init__(self,channel):
		self.channel = channel
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.channel, GPIO.IN)
		
	def getSensorValue(self):
		if GPIO.input(self.channel):
			return 0
		else:
			return 1



#def callback(channel):  
#	if GPIO.input(channel):
#		print("LED off")
#	else:
#		print("LED on")

# This line tells our script to keep an eye on our gpio pin and let us know when the pin goes HIGH or LOW
#GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
# This line asigns a function to the GPIO pin so that when the above line tells us there is a change on the pin, run this function
#GPIO.add_event_callback(channel, callback)

# This is an infinte loop to keep our script running



