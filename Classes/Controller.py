import time
from Teacher import Teacher
from Schedule import Schedule, ScheduleStatus
from TimeFrame import TimeFrame, Day
from DatabaseConnector import DatabaseConnector
import datetime
from UiLoader import UiLoader, EventCommunicator
from proposeSchedule import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QCheckBox


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
        print(self.notAvailableDates, self.proposedTimeList)

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