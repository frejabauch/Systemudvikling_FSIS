from User import User

class Teacher(User):
    def __init__(self, FirstName, LastName, PhoneNumber, Mail, TeacherID):
        User.__init__(self, FirstName, LastName, PhoneNumber, Mail)
        # self.CourseAffiliations = CourseAffiliations
        self.TeacherID = TeacherID
        #self.TeacherID = self.UserID

    def proposeSchedule(self, Schedule: list):
        mydict = {}
        mydict.update({self.name: Schedule})
        return mydict