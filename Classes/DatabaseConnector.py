import mysql.connector
from mysql.connector import errorcode
from TeacherToXML import TeacherToXML
from XMLToTeacher import XMLToTeacher
from Course import Course
from Schedule import Schedule
from TimeFrame import TimeFrame
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
        query = f"SELECT FirstName, LastName, PhoneNumber, Mail, TeacherID FROM Teacher INNER JOIN User ON User.UserID=Teacher.TeacherID WHERE TeacherID='{TeacherID}'"
        databaseCursor.execute(query)
        result = databaseCursor.fetchone()
        print(result)
        databaseCursor.close()
        if result is not None:
            return Teacher(*result)

    def saveTimeFrameToDatabase(self, inputTimeFrame: TimeFrame):
        databaseCursor = self.databaseConnection.cursor()
        query = f"INSERT INTO TimeFrame(StartTime, EndTime, Weekday, CourseID) VALUES ('{inputTimeFrame.StartTime}', '{inputTimeFrame.EndTime}', '{inputTimeFrame.Weekday.value}', '{inputTimeFrame.CourseID}');"
        databaseCursor.execute(query)
        self.databaseConnection.commit()
        print("TimeFrame saved successfully.")
        databaseCursor.close()
    
    def saveScheduleToDatabase(self, InputSchedule: Schedule):
        databaseCursor = self.databaseConnection.cursor()
        query = f"INSERT INTO Schedule(ScheduleID, StartDate, EndDate, ScheduleStatus, AdminID, EducationID, CSID) VALUES ({InputSchedule.ScheduleID}, '{InputSchedule.StartDate}', '{InputSchedule.EndDate}', '{InputSchedule.ScheduleStatus.value}', '{InputSchedule.AdminID}', {InputSchedule.EducationID}, '{InputSchedule.CSID}');"
        databaseCursor.execute(query)
        self.databaseConnection.commit()
        print(f"Schedule with ID {InputSchedule.ScheduleID} saved successfully.")
        databaseCursor.close()
    
    def saveCourseToDatabase(self, inputCourse: Course):
        databaseCursor = self.databaseConnection.cursor()
        query = f"INSERT INTO Course(CourseID, ECTS, TeacherID, Faculty, ScheduleID) VALUES ('{inputCourse.CourseID}', '{inputCourse.ECTS}', '{inputCourse.TeacherID}', '{inputCourse.Faculty}', {inputCourse.ScheduleID})"
        databaseCursor.execute(query)
        self.databaseConnection.commit()

    def loadAllTeachers(self):
        databaseCursor = self.databaseConnection.cursor()
        query = "SELECT * FROM Teacher INNER JOIN User ON User.UserID=Teacher.TeacherID"
        databaseCursor.execute(query)
        result = databaseCursor.fetchall()
        teacherObjects = [Teacher(*res[:5]) for res in result]
        ttx = TeacherToXML(teacherObjects)
        ttx.write_file()

        teacherList = XMLToTeacher("Teachers.xml").parseXML()

        teachers = teacherList.get_teachers()
        #databaseCursor = self.dbConnector.databaseConnection.cursor()
        query2 = 'INSERT into User (FirstName, LastName, Mail, PhoneNumber, UserID) VALUES (%s, %s, %s, %s, %s)'
        val = ("Kurt", "Kurtsen", "KK@mail.dk", 59283746, "KLF897")
        databaseCursor.execute(query2, val)
        self.databaseConnection.commit()



        for teacher in teachers:
            print("-" * 30)
            print()
            print("Teacher: ", getattr(teacher, "TeacherID"), getattr(teacher, "FirstName"), getattr(teacher, "LastName"), getattr(teacher, "PhoneNumber"), getattr(teacher, "Mail"))

        databaseCursor.close()


