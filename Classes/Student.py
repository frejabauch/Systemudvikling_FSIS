from User import User

class Student(User):
    def __init__(self, FirstName, LastName, PhoneNumber, Mail):
        User.__init__(self, FirstName, LastName, PhoneNumber, Mail)
    StudentID = User.UserID
    def inputInfo(Course):
        Course.Schedule.inputInfo()


newUser = Student("Peter", "Leasy", 88888888, "peter@leasy.dk")
print(newUser.StudentID)