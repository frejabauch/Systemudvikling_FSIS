import string
import random

class UserID():
    """Custom class that generates random KU-like numberplate as UserID"""
    #Random 3 letters
    rndString = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
    #Random 3 numbers
    rndNumbers = ''.join(random.choice(string.digits) for _ in range(3))
    def __new__(cls):
        #Automatically assigns UserID when new object is created
        return cls.rndString + cls.rndNumbers

class User:
    def __new__(cls, *args, **kwargs): #Prevent creating object of base 'User' class 
        if cls is User:
            raise TypeError(f"Only subclasses of '{cls.__name__}' may be instantiated")
        return super().__new__(cls)

    def __init__(self, FirstName: str, LastName: str, PhoneNumber: int, Mail: str):
        self.FirstName = FirstName
        self.LastName = LastName
        self.PhoneNumber = PhoneNumber
        self.Mail = Mail
        self.UserID = UserID()