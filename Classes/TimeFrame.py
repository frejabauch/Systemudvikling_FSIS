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
    def __init__(self, TimeFrameID: int, StartTime: datetime, EndTime: datetime, Weekday: Day):
        self.TimeFrameID = TimeFrameID
        self.StartTime = StartTime
        self.EndTime = EndTime
        self.Weekday = Weekday
    
    def fillTimeFrame(self, Location: Location, Type: TimeFrameType, RoomID):
        self.Location = Location
        self.Type = Type
        self.RoomID = RoomID


    def deleteTimeFrame():
        pass