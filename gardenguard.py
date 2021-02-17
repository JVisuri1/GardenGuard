from configparser import ConfigParser
from datetime import datetime

from mysql.connector.dbapi import Date
from SQL.sqlclient import SqlClient


config = ConfigParser()
config.read('config.ini')

dbsettings = config["database"]

dbclient = SqlClient(dbsettings["host"], dbsettings["user"], dbsettings["pass"], dbsettings["db"])

print(dbclient.readPaged(datetime.today(), datetime.today(), 1, 10))