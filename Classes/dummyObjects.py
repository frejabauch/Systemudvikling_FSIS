from Teacher import Teacher
from Teachers import Teachers

class dummyObjects:
    @staticmethod
    def create():
        teacherList = Teachers()
        teacher1 = Teacher("Bente", "Bentsen", 12345678, "Bentsen@mail.dk")
        teacher2 = Teacher("Jørgen", "Jørgensen", 23456789, "Jørgensen@mail.dk")
        teacherList.append_teachers(teacher1)
        teacherList.append_teachers(teacher2)
        return teacherList