from Teacher import Teacher
# Used sysdev cookbook

class Teachers:
    def __init__(self):
        self.teachers = []

    def append_teachers(self, teacher: Teacher):
        self.teachers.append(teacher)

    def get_teachers(self):
        return self.teachers
