from lxml import objectify
from Teacher import Teacher

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