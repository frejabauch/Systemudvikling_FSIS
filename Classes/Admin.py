from User import User

class Admin(User):
    def __init__(self, FirstName, LastName, PhoneNumber, Mail):
        User.__init__(self, FirstName, LastName, PhoneNumber, Mail)
        self.AdminID = self.UserID
    def inputInfo(Course):
        Course.Schedule.inputInfo()


newUser = Admin("Peter", "Leasy", 88888888, "peter@leasy.dk")
print(newUser.AdminID)