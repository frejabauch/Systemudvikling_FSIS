from Teacher import Teacher
from Schedule import Schedule
from TimeFrame import TimeFrame, Day
from DatabaseConnector import DatabaseConnector
import datetime

timeObject = datetime.datetime.now().time().isoformat('minutes')
dbConnector = DatabaseConnector()
dbConnector.connectToDatabase()


testFrame = TimeFrame(1, timeObject, timeObject, Day.Man)

# print("INSERT INTO TimeFrame(ScheduleID, StartTime, EndTime, Weekday) VALUES (1, '9:00', '12:00', 'Man');")

# print(f"INSERT INTO TimeFrame(ScheduleID, StartTime, EndTime, Weekday) VALUES ({testFrame.ScheduleID}, '{testFrame.StartTime}', '{testFrame.EndTime}', '{testFrame.Weekday.value}')")

# proposingTeacher = dbConnector.loadTeacherFromDatabase("ABC123")
# print(proposingTeacher.FirstName)

dbConnector.saveTimeFrameToDatabase(testFrame)
