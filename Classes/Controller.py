import time
import mysql
from Course import Course
from Teacher import Teacher
from Schedule import Schedule, ScheduleStatus
from TimeFrame import TimeFrameBuilder
from DatabaseConnector import DatabaseConnector
from datetime import datetime
from UiLoader import UiLoader, EventCommunicator
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QCheckBox
# from TeacherToXML import TeacherToXML
# from XMLToTeacher import XMLToTeacher

class Controller():

    def __init__(self, view: UiLoader):
        self.view = view
        self.eventHandler = view.eventHandler
        self.dbConnector = DatabaseConnector()
        self.dbConnector.connectToDatabase()
        # self.loadAllTeachers()
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
        semesterStart = datetime.strptime('01/02/22 07:00:00', '%d/%m/%y %H:%M:%S')
        semesterEnd = datetime.strptime('28/06/22 18:00:00', '%d/%m/%y %H:%M:%S')
        proposedSchedule = Schedule(1234, semesterStart, semesterEnd, ScheduleStatus.Proposed, "FGH345", 312, "BCD234")
        dummyCourse = Course("DummyCourse", 7.5, "ABC123", 'Science', 1234)
        self.dbConnector.saveScheduleToDatabase(proposedSchedule)
        self.dbConnector.saveCourseToDatabase(dummyCourse)
        for timeFrame in self.timeFrameList:
            self.dbConnector.saveTimeFrameToDatabase(timeFrame)
        

e = EventCommunicator()
v = UiLoader(e)
c = Controller(v)
