import unittest
from Teacher import Teacher
from UiLoader import EventCommunicator


class ProposeScheduleTests(unittest.TestCase):
    def test_teacherProposedSchedule(self):
        #Setup
        eventHandler = EventCommunicator()
        testTeacher = Teacher("Mette", "Jensen", 12345678, "mettejensen@sund.ku.dk", "ABC123")
        testTeacher.setupEventHandler(eventHandler)
        signalReceived = False
        eventHandler.proposed.connect(signalReceived = True)
        #Call
        testTeacher.proposeSchedule()
        #Assert
        self.assertNotEqual(False, signalReceived)


