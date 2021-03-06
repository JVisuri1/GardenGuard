from Sensors.air import AirSensor
from configparser import ConfigParser
import time # This is the time library, we need this so we can use the sleep function
from Sensors.groundmoisture import GroundMoistureSensor
import adafruit_dht
import board

import mysql.connector

config = ConfigParser()
config.read('config.ini')
dbsettings = config["database"]

dhtDevice = adafruit_dht.DHT22(board.D4)

while True:

    conn = mysql.connector.connect(
    host=dbsettings["host"],
    user=dbsettings["user"],
    passwd=dbsettings["pass"],
    database=dbsettings["db"])
    cursor = conn.cursor()

    sensor1 = GroundMoistureSensor(17)
    groundMoist1 = sensor1.getSensorValue()

    airSensor = AirSensor()
    temp = airSensor.getTemperature(dhtDevice)
    humidity = airSensor.getHumidity(dhtDevice)

    cursor.execute("INSERT INTO sensor_log (temp, humidity, moist1, moist2) VALUES ({:.1f},{:.1f},{},{})".format(temp, humidity, groundMoist1, 0))
    conn.commit()
    if cursor.rowcount > 0:
        print("Lämpötila: {}, ilmankosteus: {}, maankosteus1: {}, maankosteus1: null".format(temp, humidity, groundMoist1))
    
    time.sleep(60)
