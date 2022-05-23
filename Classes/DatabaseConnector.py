from sqlite3 import Time
import mysql.connector
from mysql.connector import errorcode
import getpass
from TimeFrame import TimeFrame
from Teacher import Teacher

class DatabaseConnector:
    databaseIsConnected = False
    databaseConnection: mysql.connector.MySQLConnection

    def connectToDatabase(self) -> mysql.connector.MySQLConnection:
        if not self.databaseIsConnected:
            try:
                print("Input database name:")
                databaseName = input("Database: ")
                print("Input password")
                password = getpass.getpass()
                
                self.databaseConnection = mysql.connector.connect(user="root", password=f"{password}", host="127.0.0.1", database=f'{databaseName}')
                self.databaseIsConnected = True
                print(f"Connected to database {databaseName}")
                # databaseCursor = databaseConnector.cursor()
            except mysql.connector.Error as error:
                if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Check username or password for database")


    def loadTeacherFromDatabase(self, TeacherID: str) -> Teacher:
        databaseCursor = self.databaseConnection.cursor()
        query = f"SELECT FirstName, LastName, PhoneNumber, Mail FROM Teacher INNER JOIN User ON User.UserID=Teacher.TeacherID WHERE TeacherID='{TeacherID}'"
        databaseCursor.execute(query)
        result = databaseCursor.fetchall()
        databaseCursor.close()
        return Teacher(*result[0])

    def saveTimeFrameToDatabase(self, inputTimeFrame: TimeFrame):
        databaseCursor = self.databaseConnection.cursor()
        query = f"INSERT INTO TimeFrame(ScheduleID, StartTime, EndTime, Weekday) VALUES ({inputTimeFrame.ScheduleID}, '{inputTimeFrame.StartTime}', '{inputTimeFrame.EndTime}', '{inputTimeFrame.Weekday.value}')"
        # query = "INSERT INTO new_Iter3.TimeFrame(ScheduleID, StartTime, EndTime, Weekday) VALUES(1, '9:00', '12:00', 'Man');"
        databaseCursor.execute(query)
        print("TimeFrame saved successfully")
        self.databaseConnection.commit()
        databaseCursor.close()