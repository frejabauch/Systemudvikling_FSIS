import User

class Teacher(User):
    def __init__(self, FirstName, LastName, PhoneNumber, Mail, CourseAffiliations: list):
        User.__init__(self, FirstName, LastName, PhoneNumber, Mail)
        self.CourseAffiliations = CourseAffiliations

    def proposeSchedule(self, Schedule: list):
        mydict = {}
        mydict.update({self.name: Schedule})
        return mydict