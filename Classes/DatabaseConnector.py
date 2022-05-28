import os
from sqlite3 import Time
import mysql.connector
from mysql.connector import errorcode
import getpass
from Schedule import Schedule
from TimeFrame import TimeFrame, TimeFrameBuilder
from Teacher import Teacher

class DatabaseConnector:
    databaseIsConnected = False
    databaseConnection: mysql.connector.MySQLConnection

    def connectToDatabase(self) -> mysql.connector.MySQLConnection:
        if not self.databaseIsConnected:
            try:
                print("Input database name")
                databaseName = input("Database: ")
                print("Input password")
                password = input("Password: ")

                self.databaseConnection = mysql.connector.connect(user="root", password=f"{password}", host="127.0.0.1", database=f'{databaseName}')
                self.databaseIsConnected = True
                print(f"Connected to database {databaseName}")
                # databaseCursor = databaseConnector.cursor()
            except mysql.connector.Error as error:
                if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Check username or password for database")

    def closeDatabaseConnection(self):
        if self.databaseIsConnected:
            self.databaseConnection.close()

    def loadTeacherFromDatabase(self, TeacherID: str) -> Teacher:
        databaseCursor = self.databaseConnection.cursor()
        query = f"SELECT FirstName, LastName, PhoneNumber, Mail FROM Teacher INNER JOIN User ON User.UserID=Teacher.TeacherID WHERE TeacherID='{TeacherID}'"
        databaseCursor.execute(query)
        result = databaseCursor.fetchone()
        print(result)
        databaseCursor.close()
        if result is not None:
            return Teacher(*result)

    def saveTimeFrameToDatabase(self, inputTimeFrame: TimeFrame):
        databaseCursor = self.databaseConnection.cursor()
        query = f"INSERT INTO TimeFrame(ScheduleID, StartTime, EndTime, Weekday) VALUES ({inputTimeFrame.TimeFrameID}, '{inputTimeFrame.StartTime}', '{inputTimeFrame.EndTime}', '{inputTimeFrame.Weekday.value}');"
        # query = "INSERT INTO new_Iter3.TimeFrame(ScheduleID, StartTime, EndTime, Weekday) VALUES(1, '9:00', '12:00', 'Man');"
        databaseCursor.execute(query)
        self.databaseConnection.commit()
        print("TimeFrame saved successfully.")
        databaseCursor.close()
    
    def saveScheduleToDatabase(self, InputSchedule: Schedule):
        databaseCursor = self.databaseConnection.cursor()
        query = f"INSERT INTO Schedule(ScheduleID, StartDate, EndDate, ScheduleStatus, CourseID, AdminID, EducationID, CSID) VALUES ({InputSchedule.ScheduleID}, '{InputSchedule.StartDate}', '{InputSchedule.EndDate}', '{InputSchedule.ScheduleStatus.value}', '{InputSchedule.CourseID}', '{InputSchedule.AdminID}', {InputSchedule.EducationID}, '{InputSchedule.CSID}');"
        print(query)
        print("INSERT into Schedule(ScheduleID, StartDate, EndDate, ScheduleStatus, CourseID, AdminID, EducationID, CSID) Values (NULL, '2022-02-01', '2022-07-01', 'Confirmed', 'NDAB19000U', 'FGH345', 312, 'BCD234');")
        databaseCursor.execute(query)
        self.databaseConnection.commit()
        print(f"Schedule with ID {InputSchedule.ScheduleID} saved successfully.")
        databaseCursor.close()

