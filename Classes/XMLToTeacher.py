from lxml import objectify
from Teacher import Teacher
from Teachers import Teachers

# Used sysdev cookbook

class XMLToTeacher:
    def __init__(self, xml_filename):
        self.xml_filename = xml_filename

    def parseXML(self) -> Teachers:
        with open(self.xml_filename, "rb") as f:
            xml = f.read()

        root = objectify.fromstring(xml)

        teacherList = Teachers()

        for teacher in root.getchildren():
            teacher_obj = Teacher(teacher.FirstName, teacher.LastName, teacher.PhoneNumber, teacher.Mail, teacher.TeacherID)

            teacherList.append_teachers(teacher_obj)
        return teacherList
