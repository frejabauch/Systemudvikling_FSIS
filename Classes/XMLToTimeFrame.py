from lxml import objectify
from TimeFrame import TimeFrame
from Timeframes import TimeFrames

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

            timeframeList.append_timeframes(timeframe_obj)
        return timeframeList