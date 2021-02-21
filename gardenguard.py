from configparser import ConfigParser
import time # This is the time library, we need this so we can use the sleep function
from Sensors.groundmoisture import GroundMoistureSensor

import mysql.connector

while True:
    config = ConfigParser()
    config.read('config.ini')
    dbsettings = config["database"]
    conn = mysql.connector.connect(
    host=dbsettings["host"],
    user=dbsettings["user"],
    passwd=dbsettings["pass"],
    database=dbsettings["db"])
    cursor = conn.cursor()
    sensor1=GroundMoistureSensor(17)
    value1 = sensor1.getSensorValue()

    cursor.execute("INSERT INTO sensor_log (temp, humidity, moist1, moist2) VALUES ({},{},{},{})".format(0, 0, value1, 0))
    conn.commit()
    print(cursor.rowcount, "record inserted.")
    
    time.sleep(5)
