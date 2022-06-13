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
        self.dbConnector.loadAllTeachers()
        self.dbConnector.loadAllTimetables()
        self.setupEventConnections()
        self.view.loadUi()


    def setupEventConnections(self):
        self.eventHandler.loginPressed.connect(self.loadTeacher)
        self.eventHandler.loginSuccess.connect(self.setUiTeacher)
        self.eventHandler.loginSuccess.connect(self.view.loginWindow.close)
        self.eventHandler.loginSuccess.connect(self.view.frontPageWindow.show)
        self.eventHandler.proposed.connect(self.loadProposedSchedule)
        self.eventHandler.proposed.connect(self.insertSchedule)

    def setUiTeacher(self):
        self.view.displayTeacher(self.teacher.FirstName + " " + self.teacher.LastName)

    def loadTeacher(self):
        self.inputID = self.view.loginWindow.userID
        self.teacher = self.dbConnector.loadTeacherFromDatabase(self.inputID)
        if self.teacher is not None:
            self.eventHandler.loginSuccess.emit()
        
    def loadProposedSchedule(self):
        self.notAvailableDates = self.view.proposeWindow.notAvailableDateList
        self.proposedTimeList = self.view.proposeWindow.proposedTimeList
        builder = TimeFrameBuilder(self.proposedTimeList)
        self.timeFrameList = builder.createTimeFrameList("DummyCourse")

    def insertSchedule(self):
        proposedSchedule = self.teacher.proposeSchedule()
        dummyCourse = Course("DummyCourse", 7.5, "ABC123", 'Science', 1234)
        self.dbConnector.saveScheduleToDatabase(proposedSchedule)
        self.dbConnector.saveCourseToDatabase(dummyCourse)
        for timeFrame in self.timeFrameList:
            self.dbConnector.saveTimeFrameToDatabase(timeFrame)
        
