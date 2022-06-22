class Course():
    def __init__(self, CourseID, ECTS, TeacherID, Faculty, ScheduleID):
        self.CourseID = CourseID
        self.ECTS = ECTS
        self.TeacherID = TeacherID
        self.Faculty = Faculty
        self.ScheduleID = ScheduleID
        self.TimeFrames = []
    
    def addTimeFrame(self, inputFrame):
        self.TimeFrames.append(inputFrame)