from datetime import datetime
from enum import Enum

class Day(Enum):
    Man = 1
    Tirs = 2
    Ons = 3
    Tors = 4
    Fre = 5

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