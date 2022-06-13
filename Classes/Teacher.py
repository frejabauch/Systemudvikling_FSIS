from datetime import datetime
from Schedule import Schedule, ScheduleStatus
from User import User

class Teacher(User):
    def __init__(self, FirstName, LastName, PhoneNumber, Mail, TeacherID):
        User.__init__(self, FirstName, LastName, PhoneNumber, Mail)
        self.TeacherID = TeacherID
        #self.TeacherID = self.UserID

    def proposeSchedule(self):
        semesterStart = datetime.strptime('01/02/22 07:00:00', '%d/%m/%y %H:%M:%S')
        semesterEnd = datetime.strptime('28/06/22 18:00:00', '%d/%m/%y %H:%M:%S')
        return Schedule(1234, semesterStart, semesterEnd, ScheduleStatus.Proposed, "FGH345", 312, "BCD234")