from lxml import objectify
from TimeFrame import TimeFrame, ClassType
from Timeframes import TimeFrames

# Used sysdev cookbook

class XMLToTimeFrame:
    def __init__(self, xml_filename):
        self.xml_filename = xml_filename

    def parseXML(self) -> TimeFrames:
        with open(self.xml_filename, "rb") as f:
            xml = f.read()

        root = objectify.fromstring(xml)

        timeframeList = TimeFrames()

        for timeframe in root.getchildren():
            timeframe_obj = TimeFrame(timeframe.StartTime, timeframe.EndTime, timeframe.Weekday, timeframe.CourseID)
            timeframe_obj.fillTimeFrame(timeframe.ClassType, timeframe.RoomID)

            timeframeList.append_timeframes(timeframe_obj)
        return timeframeList