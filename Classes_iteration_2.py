from datetime import datetime

class User():
    def __init__(self, name, PersonalInfo, ContactInfo, Role):
        self.name = name
        self.PersonalInfo = PersonalInfo
        self.ContactInfo = ContactInfo
        self.Role = Role

class Schedule():
    def __init__(self, Classes, Date: datetime):
        self.Classes = Classes
        self.Date = Date
    
    def __init__(self, TimeFrame, Date: datetime):
        self.TimeFrame = TimeFrame
        self.Date = Date

    def proposeSchedule():
        pass

    def createSchedule():
        pass

    def updateSchedule():
        pass

    def viewSchedule():
        pass

    def inputInfo():
        pass


class Course():
    def __init__(self, Schedule, ECTS, CourseID, StudentList, Teacher, Location):
        self.Schedule = Schedule
        self.ECTS = ECTS
        self.CourseID = CourseID
        self.StudentList = StudentList
        self.Teacher = Teacher
        self.Location = Location

class Teacher(User):
    def __init__(self, name, PersonalInfo, ContactInfo, Role, CourseAffiliations: list):
        User.__init__(self, name, PersonalInfo, ContactInfo, Role)
        self.CourseAffiliations = CourseAffiliations

    def proposeSchedule(self, Schedule: list):
        mydict = {}
        mydict.update({self.name: Schedule})
        return mydict


class Admin(User):
    def __init__(self, name, PersonalInfo, ContactInfo, Role, Admin):
        User.__init__(self, name, PersonalInfo, ContactInfo, Role)
        self.Admin = Admin

    def inputInfo(Course):
        Course.Schedule.inputInfo()

class CourseSecretary(User):
    def __init__(self, name, PersonalInfo, ContactInfo, Role, Course_secretary):
        User.__init__(self, name, PersonalInfo, ContactInfo, Role)
        self.Course_secretary = Course_secretary

    def createSchedule(Course):
        Course.Schedule.createSchedule()

class TimeFrame():
    def __init__(self, StartTime: datetime, EndTime: datetime):
        self.StartTime = StartTime
        self.EndTime = EndTime
    
    def updateTimeFrame():
        pass

    def deleteTimeFrame():
        pass