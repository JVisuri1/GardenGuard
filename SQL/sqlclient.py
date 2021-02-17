import mysql.connector

class SqlClient:
    def __init__(self, host, user, pw, db):
        self.conn = self.initCursor(host, user, pw, db)

    def __del__(self):
        self.conn.close()

    def readPaged(self, startDate, endDate, page, pageSize):
        self.conn.execute("SELECT * FROM sensor_log")
    
    def initCursor(self, host, user, pw, db):
        conn = mysql.connector.connect(
        host=host,
        user=user,
        passwd=pw,
        database=db
        )
        return conn.cursor()




# CREATE DATABASE GardenGuardDB
# CREATE TABLE sensor_log (id INT AUTO_INCREMENT PRIMARY KEY, log_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, temp DECIMAL (4,2), humidity DECIMAL (4,2), moist1 BOOLEAN, moist2, BOOLEAN)
