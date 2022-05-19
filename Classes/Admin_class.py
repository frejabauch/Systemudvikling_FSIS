From User_class import User

class Admin(User):
    def __init__(self, name, PersonalInfo, ContactInfo, Role, Admin):
        User.__init__(self, name, PersonalInfo, ContactInfo, Role)
        self.Admin = Admin

    def inputInfo(Course):
        Course.Schedule.inputInfo()