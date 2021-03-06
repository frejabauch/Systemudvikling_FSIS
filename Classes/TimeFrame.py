from datetime import datetime
from enum import Enum
from datetime import datetime
from pyparsing import empty
from Location import Location

class ClassType(Enum):
    """Custom type for TimeFrame"""
    Lecture = "Lecture"
    Class = "Class"
    Meeting = "Meeting"

class Day(Enum):
    """Custom type for weekday"""
    Mon = "Mon"
    Tue = "Tue"
    Wed = "Wed"
    Thu = "Thu"
    Fri = "Fri"

class TimeFrameBuilder():
    """Class that builds TimeFrames from GUI input"""
    def __init__(self, UiList):
        #List of selected timeframes from GUI
        self.UiList = UiList
    
    def createTimeFrameList(self, CourseID):
        """Method that creates list of TimeFrames with specified CourseID"""
        TimeFrameList = []
        if any(self.UiList):
            for uiSelection in self.UiList:
                #For each element in list of selected timeframes create timeframe attributes
                weekday = Day(uiSelection[:3])
                startTime = int(uiSelection[3:5])
                endTime = startTime + 1
                startTime = datetime.strptime(str(startTime) + ":00", "%H:%M")
                endTime = datetime.strptime(str(endTime) + ":00", "%H:%M")
                #Add finished TimeFrame to list of TimeFrames
                TimeFrameList.append(TimeFrame(startTime, endTime, weekday, CourseID))
        return TimeFrameList

class TimeFrame():
    def __init__(self, StartTime: datetime, EndTime: datetime, Weekday: Day, CourseID: str):
        #TimeFrameID set by auto-increment in database
        self.TimeFrameID = None
        self.StartTime = StartTime
        self.EndTime = EndTime
        self.Weekday = Weekday
        self.CourseID = CourseID
    
    def fillTimeFrame(self, ClassType: ClassType, RoomID):
        #Placeholder method for eg. course secretary to fill in remaining information
        self.ClassType = ClassType
        self.RoomID = RoomID

    def setLocation(self, inputLocation: Location):
        self.Location = inputLocation

    def updateID(self, ID):
        self.TimeFrameID = ID
