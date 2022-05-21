from datetime import datetime
from enum import Enum
import TimeFrame

class ScheduleStatus(Enum):
    Incomplete = 1
    Proposed = 2
    Confirmed = 3

class Schedule():
    def __init__(self, Classes, StartDate: datetime, EndDate: datetime, ScheduleID: int, Status: ScheduleStatus):
        self.Classes = Classes
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.ScheduleID = ScheduleID
        self.Status = Status

    def __init__(self, TimeFrame: TimeFrame, Date: datetime):
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