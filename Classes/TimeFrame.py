from datetime import datetime
from enum import Enum
from Location import Location

class TimeFrameType(Enum):
    Lecture = 1
    Class = 2
    Meeting = 3

class Day(Enum):
    Mon = "Mon"
    Tue = "Tue"
    Wed = "Wed"
    Thu = "Thu"
    Fri = "Fri"

# class TimeFrameBuilder():

class TimeFrame():
    def __init__(self, ScheduleID: int, StartTime: datetime, EndTime: datetime, Weekday: Day, ClassLocation: Location, ClassType: TimeFrameType):
        self.ScheduleID = ScheduleID
        self.StartTime = StartTime
        self.EndTime = EndTime
        self.Weekday = Weekday
        self.ClassLocation = ClassLocation
        self.ClassType = ClassType
    
    def updateTimeFrame():
        pass

    def deleteTimeFrame():
        pass