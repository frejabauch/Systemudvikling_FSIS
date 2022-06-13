from datetime import datetime
from enum import Enum

from Course import Course

class ScheduleStatus(Enum):
    """Custom type for status of Schedule"""
    Incomplete = "Incomplete"
    Proposed = "Proposed"
    Confirmed = "Confirmed"

class Schedule():
    def __init__(self, StartDate: datetime, EndDate: datetime, ScheduleStatus: ScheduleStatus, AdminID: str, EducationID: int, CSID: str):
        #ScheduleID assigned by auto increment in database
        #self.ScheduleID = ScheduleID
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.ScheduleStatus = ScheduleStatus
        self.AdminID = AdminID
        self.EducationID = EducationID
        self.CSID = CSID
        self.CourseList = []
    
    def addCourse(self, inputCourse: Course):
        self.CourseList.append(inputCourse)
