From User_class import User

class Teacher(User):
    def __init__(self, name, PersonalInfo, ContactInfo, Role, CourseAffiliations: list):
        User.__init__(self, name, PersonalInfo, ContactInfo, Role)
        self.CourseAffiliations = CourseAffiliations

    def proposeSchedule(self, Schedule: list):
        mydict = {}
        mydict.update({self.name: Schedule})
        return mydict