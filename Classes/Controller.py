import time
from Teacher import Teacher
from Schedule import Schedule, ScheduleStatus
from TimeFrame import TimeFrame, Day
from DatabaseConnector import DatabaseConnector
import datetime

timeObject = datetime.datetime.now()
dbConnector = DatabaseConnector()
dbConnector.connectToDatabase()


testFrame = TimeFrame(1, timeObject, timeObject, Day.Man)
testSchedule = Schedule(1234, timeObject, timeObject, ScheduleStatus.Confirmed, "NDAB19000U", "FGH345", 312, "BCD234")

# proposingTeacher = dbConnector.loadTeacherFromDatabase("ABC123")
# print(proposingTeacher.FirstName)

# dbConnector.saveTimeFrameToDatabase(testFrame)
dbConnector.saveScheduleToDatabase(testSchedule)

dbConnector.closeDatabaseConnection()