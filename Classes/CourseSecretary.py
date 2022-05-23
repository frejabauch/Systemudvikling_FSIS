import User

class CourseSecretary(User):
    def __init__(self, name, PersonalInfo, ContactInfo, Role, Course_secretary):
        User.__init__(self, name, PersonalInfo, ContactInfo, Role)
        self.Course_secretary = Course_secretary
        self.CSID = self.UserID

    def createSchedule(Course):
        Course.Schedule.createSchedule()