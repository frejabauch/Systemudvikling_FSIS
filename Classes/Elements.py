from lxml import objectify
from Teacher import Teacher
from TimeFrame import TimeFrame

#Inspiration sysdev cookbook

class Elements:
    @staticmethod
    def create_teacher(teacher_obj: Teacher):
        teacher = objectify.Element("teach")
        teacher.FirstName = getattr(teacher_obj, "FirstName")
        teacher.LastName = getattr(teacher_obj, "LastName")
        teacher.PhoneNumber = getattr(teacher_obj, "PhoneNumber")
        teacher.Mail = getattr(teacher_obj, "Mail")
        teacher.TeacherID = getattr(teacher_obj, "TeacherID")
        return teacher

    @staticmethod
    def create_timeframe(timeframe_obj: TimeFrame):
        timeframe = objectify.Element("times")
        timeframe.TimeFrameID = getattr(timeframe_obj, "TimeFrameID")
        timeframe.StartTime = getattr(timeframe_obj, "StartTime")
        timeframe.EndTime = getattr(timeframe_obj, "EndTime")
        timeframe.Weekday = getattr(timeframe_obj, "Weekday")
        timeframe.CourseID = getattr(timeframe_obj, "CourseID")
        timeframe.ClassType = getattr(timeframe_obj, "ClassType").value
        timeframe.RoomID = getattr(timeframe_obj, "RoomID")
        return timeframe