from datetime import datetime
from enum import Enum
import TimeFrame

class ScheduleStatus(Enum):
    Incomplete = "Incomplete"
    Proposed = "Proposed"
    Confirmed = "Confirmed"

class Schedule():
    def __init__(self, ScheduleID: int, StartDate: datetime, EndDate: datetime, ScheduleStatus: ScheduleStatus, CourseID: str, AdminID: str, EducationID: int, CSID: str):
        self.ScheduleID = ScheduleID
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.ScheduleStatus = ScheduleStatus
        self.CourseID = CourseID
        self.AdminID = AdminID
        self.EducationID = EducationID
        self.CSID = CSID

    # def __init__(self, TimeFrame: TimeFrame, Date: datetime):
    #     self.TimeFrame = TimeFrame
    #     self.Date = Date

    def proposeSchedule():
        pass

    def createSchedule():
        pass

    def updateSchedule():
        pass

    def viewSchedule():
        pass