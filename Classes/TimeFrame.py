from datetime import datetime
from enum import Enum

class Day(Enum):
    Mon = "Mon"
    Tue = "Tue"
    Wed = "Wed"
    Thu = "Thu"
    Fri = "Fri"

# class TimeFrameBuilder():


class TimeFrame():
    def __init__(self, ScheduleID: int, StartTime: datetime, EndTime: datetime, Weekday: Day):
        self.ScheduleID = ScheduleID
        self.StartTime = StartTime
        self.EndTime = EndTime
        self.Weekday = Weekday
    
    def updateTimeFrame():
        pass

    def deleteTimeFrame():
        pass