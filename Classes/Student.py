from User import User

class Student(User):
    def __init__(self, FirstName, LastName, PhoneNumber, Mail):
        User.__init__(self, FirstName, LastName, PhoneNumber, Mail)
        self.StudentID = self.UserID