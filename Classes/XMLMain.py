
from dummyObjects import dummyObjects
from TeacherToXML import TeacherToXML
from XMLToTeacher import XMLToTeacher

if __name__ == "__main__":

    teacherList = dummyObjects.create()
    TeacherToXML(teacherList).write_file()

    teacherList = XMLToTeacher("teachers.xml").parseXML()

    teachers = teacherList.get_teachers()

    for teacher in teachers:
        print("-" * 30)
        print()
        print("Teacher: ", getattr(teacher, "FirstName"), getattr(teacher, "LastName"), getattr(teacher, "PhoneNumber"), getattr(teacher, "Mail"))


