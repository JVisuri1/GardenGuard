import RPi.GPIO as GPIO

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

# CREATE DATABASE GardenGuardDB
# CREATE TABLE sensor_log (id INT AUTO_INCREMENT PRIMARY KEY, log_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, temp DECIMAL (4,2), humidity DECIMAL (4,2), moist1 BOOLEAN, moist2, BOOLEAN)

