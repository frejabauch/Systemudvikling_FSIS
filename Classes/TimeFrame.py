from datetime import datetime
from enum import Enum
from datetime import datetime
from pyparsing import empty
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

class TimeFrameBuilder():
    def __init__(self, UiList, TimeFrameID):
        self.UiList = UiList
        self.TimeFrameID = TimeFrameID
    
    def createTimeFrame(self):
        TimeFrameList = []
        if any(self.UiList):
            for uiSelection in self.UiList:
                weekday = Day(uiSelection[:3])
                startTime = int(uiSelection[3:5])
                endTime = startTime + 1
                startTime = datetime.strptime(str(startTime) + ":00", "%H:%M")
                endTime = datetime.strptime(str(endTime) + ":00", "%H:%M")
                TimeFrameList.append(TimeFrame(self.TimeFrameID, startTime, endTime, weekday))
        return TimeFrameList

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