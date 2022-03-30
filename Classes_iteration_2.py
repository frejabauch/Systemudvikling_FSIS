#constructor - hvad skal der til for at lave en employee

from datetime import datetime


class User():
    def __init__(self, name, UserSchedule, PersonalInfo, ContactInfo):
        self.name = name
        self.UserSchedule = UserSchedule
        self.PersonalInfo = PersonalInfo
        self.Contactinfo = ContactInfo

    # def set_name():
    #         pass

    # def get_name():
    #         pass
    #Tror ikke ovenstående er nødvendige
class Schedule():
    def __init__(self, Classes, Date: datetime) -> None:
        self.Classes = Classes
        self.Date = Date
    
    def __init__(self, TimeFrame, Date: datetime) -> None:
        self.TimeFrame = TimeFrame
        self.Date = Date


    def updateSchedule():
        pass

    def viewSchedule():
        pass

    def proposeSchedule() -> None:
        pass

class Course():
    Schedule: Schedule
    def __init__(self, Schedule, ECTS, CourseID, ER, Responsible) -> None:
        self.Schedule = Schedule
        self.ECTS = ECTS
        self.CourseID = CourseID
        self.EnrolledStudents = ER
        self.Responsible = Responsible

class Teacher(User):
    def __init__(self, CourseAffiliations: list):
        self.CourseAffiliations = CourseAffiliations

    def proposeSchedule(Course: Course, ):
        Course.Schedule.proposeSchedule()




class TimeFrame():
    def __init__(self, StartTime: datetime, EndTime: datetime) -> None:
        self.StartTime = StartTime
        self.EndTime = EndTime
    
    def updateTimeFrame():
        pass

    def deleteTimeFrame():
        pass
    

