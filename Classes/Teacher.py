from datetime import datetime
from Schedule import Schedule, ScheduleStatus
from User import User

class Teacher(User):
    def __init__(self, FirstName, LastName, PhoneNumber, Mail, TeacherID):
        User.__init__(self, FirstName, LastName, PhoneNumber, Mail)
        self.TeacherID = TeacherID
        #self.TeacherID = self.UserID

    def setupEventHandler(self, eventHandler):
        self.eventHandler = eventHandler


    def proposeSchedule(self):
        self.eventHandler.proposed.emit()
        