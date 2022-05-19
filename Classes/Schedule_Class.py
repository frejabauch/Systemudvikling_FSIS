from datetime import datetime
from enum import Enum

class ScheduleStatus(Enum):
    Incomplete = 1
    Proposed = 1
    Confirmed = 1

class Schedule():
    def __init__(self, Classes, StartDate: datetime, EndDate: datetime, ScheduleID: int, Status: ScheduleStatus):
        self.Classes = Classes
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.ScheduleID = ScheduleID
        self.Status = Status

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