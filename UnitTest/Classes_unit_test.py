import unittest
import Classes_iteration_2

class ProposeScheduleTests(unittest.TestCase):
    def test_DisplayTeacherName(self):
        #Setup
        testTeacher = Classes_iteration_2.Teacher("Gitte", "", "", "Teacher", [])
        #Call
        scheduleDict = testTeacher.proposeSchedule([""])
        keyList = list(scheduleDict.keys())
        #Assert
        self.assertEqual(keyList[0], "Gitte")

    def test_ScheduleSavedCorrectly(self):
        #Setup
        testTeacher = Classes_iteration_2.Teacher("Gitte", "", "", "Teacher", [])
        expectedOutput = ["a", "b", "c", "d", "e", "f", "g"]
        #Call
        scheduleDict = testTeacher.proposeSchedule(["a", "b", "c", "d", "e", "f", "g"])
        dictSavedSchedule = scheduleDict["Gitte"]
        #Assert
        self.assertEqual(expectedOutput, dictSavedSchedule)
    
    def test_ScheduleIsReplaced(self):
        #Setup
        testTeacher = Classes_iteration_2.Teacher("Gitte", "", "", "Teacher", [])
        #Call
        scheduleDict = testTeacher.proposeSchedule(["a", "b", "c", "d", "e", "f", "g"])
        newScheduleDict = testTeacher.proposeSchedule([1, 2, 3, 4, 5, 6, 7])
        #Assert
        #Check testTeacher returns only latest proposed schedule
        self.assertEqual(newScheduleDict["Gitte"], [1, 2, 3, 4, 5, 6, 7])

        #Check the element "a" exists in the first dictionary
        self.assertTrue("a" in scheduleDict["Gitte"])

        #Check the element "a" doesn't exist in the updated dictionary
        self.assertFalse("a" in newScheduleDict["Gitte"])

