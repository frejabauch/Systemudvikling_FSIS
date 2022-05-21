import string
import random

class UserID():
    rndString = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
    rndNumbers = ''.join(random.choice(string.digits) for _ in range(3))
    def __new__(cls):
        return cls.rndString + cls.rndNumbers

    

class User():

    UserID = UserID()
    def __init__(self, FirstName: str, LastName: str, PhoneNumber: int, Mail: str):
        self.FirstName = FirstName
        self.LastName = LastName
        self.PhoneNumber = PhoneNumber
        self.Mail = Mail

newUser = User("Peter", "Leasy", 88888888, "peter@leasy.dk")
print(newUser.UserID)