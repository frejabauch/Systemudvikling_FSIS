from datetime import datetime
import unittest
from Course import Course
from Schedule import Schedule, ScheduleStatus
from Teacher import Teacher
from UiLoader import EventCommunicator


class ProposeScheduleTest(unittest.TestCase):
    def test_teacherProposedSchedule(self):
        #Setup
        self.signalReceived = False
        def setTrue(self):
            self.signalReceived = True

        eventHandler = EventCommunicator()
        eventHandler.proposed.connect(lambda: setTrue(self))
        
        testTeacher = Teacher("Mette", "Jensen", 12345678, "mettejensen@sund.ku.dk", "ABC123")
        testTeacher.setupEventHandler(eventHandler)
        #Call
        testTeacher.proposeSchedule()
        #Assert
        self.assertEqual(True, self.signalReceived)

class ScheduleTest(unittest.TestCase):
    def test_addCourseToSchedule(self):
        #Setup
        testSchedule = Schedule(datetime.now, datetime.now, ScheduleStatus.Incomplete, "ABC123", 1, "DEF456")
        testCourse = Course("TestCourse", 0, "ABC123", "Science", 1)

        #Call
        testSchedule.addCourse(testCourse)
        #Assert
        self.assertTrue(len(testSchedule.CourseList) > 0)
