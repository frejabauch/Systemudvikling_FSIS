from User import User

class Admin(User):
    """Creates subclass of User class with AdminID as inherited UserID"""
    def __init__(self, FirstName, LastName, PhoneNumber, Mail):
        User.__init__(self, FirstName, LastName, PhoneNumber, Mail)
        self.AdminID = self.UserID
    
    def CreateSchedule():
        pass

    def ViewSchedule():
        pass

    def EditSchedule():
        pass