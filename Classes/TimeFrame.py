from datetime import datetime
from enum import Enum

class Day(Enum):
    Man = "Man"
    Tirs = "Tirs"
    Ons = "Ons"
    Tors = "Tors"
    Fre = "Fre"

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