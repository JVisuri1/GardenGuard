# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_dht

class AirSensor:
    def __init__(self):
        dhtDevice = adafruit_dht.DHT22(board.D4)

    def getTemperature(self):
        try:
            return self.dhtDevice.temperature
        except RuntimeError as error:
            print(error.args[0])
            return 0

    def getHumidity(self):
        try:
            return self.dhtDevice.humidity
        except RuntimeError as error:
            print(error.args[0])
            return 0
