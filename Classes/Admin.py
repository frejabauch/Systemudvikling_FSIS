import User

class Admin(User):
    def __init__(self, FirstName, LastName, PhoneNumber, Mail, AdminID):
        User.__init__(self, FirstName, LastName, PhoneNumber, Mail)

    def inputInfo(Course):
        Course.Schedule.inputInfo()