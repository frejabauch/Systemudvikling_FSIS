import time
from Course import Course
from Teacher import Teacher
from Schedule import Schedule, ScheduleStatus
from TimeFrame import TimeFrameBuilder
from DatabaseConnector import DatabaseConnector
from datetime import datetime
from UiLoader import UiLoader, EventCommunicator



class Controller():

    def __init__(self, view: UiLoader):
        self.view = view
        self.eventHandler = view.eventHandler
        self.dbConnector = DatabaseConnector()
        self.dbConnector.connectToDatabase()
        self.setupEventConnections()
        self.view.loadUi()

    def setupEventConnections(self):
        # self.eventHandler.loginPressed.connect(self.setUiTeacher("Mette", "Jensen"))
        print(callable(self.loadTeacher))
        self.eventHandler.loginPressed.connect(self.loadTeacher)
        self.eventHandler.loginSuccess.connect(self.setUiTeacher)
        self.eventHandler.loginSuccess.connect(self.view.loginWindow.close)
        self.eventHandler.loginSuccess.connect(self.view.frontPageWindow.show)
        self.eventHandler.proposed.connect(self.loadProposedSchedule)
        self.eventHandler.proposed.connect(self.insertSchedule)
        # self.eventHandler.loginFailed.connect(self.view.)

    def setUiTeacher(self):
        self.view.displayTeacher(self.teacher.FirstName + " " + self.teacher.LastName)

    def loadTeacher(self):
        self.inputID = self.view.loginWindow.userID
        self.teacher = self.dbConnector.loadTeacherFromDatabase(self.inputID)
        if self.teacher is not None:
            self.eventHandler.loginSuccess.emit()
        
        # Implementer evt fejlmeddelelse?
        # else: 
        #     print("Failed to load Teacher")
        #     self.eventHandler.loginFailed.emit()
        
    def loadProposedSchedule(self):
        self.notAvailableDates = self.view.proposeWindow.dateList
        self.proposedTimeList = self.view.proposeWindow.proposedTimeList
        builder = TimeFrameBuilder(self.proposedTimeList, 123)
        self.timeFrameList = builder.createTimeFrame()
        # for i in timeFrameList:
        #     print(i.TimeFrameID, i.StartTime, i.EndTime, i.Weekday)
        # print(self.notAvailableDates, timeFrameList)

    def insertSchedule(self):
        semesterStart = datetime.strptime('01/02/22 07:00:00', '%d/%m/%y %H:%M:%S')
        semesterEnd = datetime.strptime('28/06/22 18:00:00', '%d/%m/%y %H:%M:%S')
        proposedSchedule = Schedule(1234, semesterStart, semesterEnd, ScheduleStatus.Proposed, "DummyCourse", "FGH345", 312, "BCD234")
        dummyCourse = Course("DummyCourse", 7.5, 123, "ABC123", 'Science')
        for timeFrame in self.timeFrameList:
            self.dbConnector.saveTimeFrameToDatabase(timeFrame)
        self.dbConnector.saveCourseToDatabase(dummyCourse)
        self.dbConnector.saveScheduleToDatabase(proposedSchedule)


e = EventCommunicator()
v = UiLoader(e)
c = Controller(v)


# timeObject = datetime.datetime.now()



# testFrame = TimeFrame(1, timeObject, timeObject, Day.Man)
# testSchedule = Schedule(1234, timeObject, timeObject, ScheduleStatus.Confirmed, "NDAB19000U", "FGH345", 312, "BCD234")

# proposingTeacher = dbConnector.loadTeacherFromDatabase("ABC123")
# print(proposingTeacher.FirstName)

# # dbConnector.saveTimeFrameToDatabase(testFrame)
# dbConnector.saveScheduleToDatabase(testSchedule)

# dbConnector.closeDatabaseConnection()