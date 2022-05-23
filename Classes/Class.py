from enum import Enum
from Location import Location
import datetime

class ClassType(Enum):
    Lecture = 1
    Class = 2
    Meeting = 3

class Class():
    def __init__(self, StartTime: datetime, EndTime: datetime, ClassLocation: Location, ClassType: ClassType) -> None:
        self.StartTime = StartTime
        self.EndTime = EndTime
        self.ClassLocation = ClassLocation
        self.ClassType = ClassType