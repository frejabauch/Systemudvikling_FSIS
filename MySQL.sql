SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE Location;
DROP TABLE Course;
DROP TABLE Class;
DROP TABLE Schedule;
DROP TABLE User;
DROP TABLE Student;
DROP TABLE Admin;
DROP TABLE Teacher;
DROP TABLE CourseSecretary;
DROP TABLE Education;
SET FOREIGN_KEY_CHECKS = 1;
CREATE TABLE IF NOT EXISTS `Education` (
	`EducationID` int NOT NULL, #Skal ikke være tilfældigt
    `Title` VARCHAR(255),
    `University` enum('KU', 'DTU'),
    PRIMARY KEY(`EducationID`)
);

CREATE TABLE IF NOT EXISTS `User`(
	`FirstName` VARCHAR(255),
    `LastName` VARCHAR(255),
    `Mail` VARCHAR(255),
    `PhoneNumber` int,
    `UserID` int,
    PRIMARY KEY (`UserID`)
);

CREATE TABLE IF NOT EXISTS `Location`(
  `RoomID` int NOT NULL,
  `Address` VARCHAR(255),
  `Location_Type` enum('Lecture hall','Classroom','Study hall','Study room') DEFAULT NULL,
  `Capacity` int DEFAULT NULL,
  PRIMARY KEY (`RoomID`)
);

CREATE TABLE IF NOT EXISTS `Teacher`(
    `TeacherID` VARCHAR(6),
    `UserID` int,
    PRIMARY KEY (`TeacherID`),
    KEY `fk_teacher_UserID_idx` (`UserID`),
    CONSTRAINT `fk_teacher_UserID` FOREIGN KEY (`UserID`) REFERENCES `User`(`UserID`)
);

CREATE TABLE IF NOT EXISTS `CourseSecretary`(
	`CSID` VARCHAR(6),
    `UserID` int,
    PRIMARY KEY (`CSID`),
    FOREIGN KEY (`UserID`) REFERENCES `User`(`UserID`)
);

CREATE TABLE IF NOT EXISTS `Admin`(
	`AdminID` VARCHAR(6),
    `UserID` int,
    PRIMARY KEY (`AdminID`),
    FOREIGN KEY (`UserID`) REFERENCES `User`(`UserID`)
);

CREATE TABLE IF NOT EXISTS `Class`(
  `ClassID` int NOT NULL AUTO_INCREMENT,
  `Time` datetime DEFAULT NULL,
  `ClassType` enum('Lecture','class','meeting') DEFAULT NULL,
  `TeacherID` VARCHAR(6), #Teacher ID har vi sat som værende 6 karaktere, mere specifikt 3 bogstaver 3 tal. 
  `RoomID` int DEFAULT NULL,
  `CourseID` int NOT NULL,
  PRIMARY KEY (`ClassID`),
  FOREIGN KEY (`RoomID`) REFERENCES `Location`(`RoomID`)
);

CREATE TABLE IF NOT EXISTS `Course`(
  `CourseID` int NOT NULL,
  `ScheduleID` int,
  `ECTS` float DEFAULT NULL,
  `ClassID` int NOT NULL AUTO_INCREMENT,
  `TeacherID` varchar(50) DEFAULT NULL,
  `Faculty` enum('SUND', 'HUM', 'JURA', 'Science', 'SAMF', 'TEOL', 'DTU'),
  PRIMARY KEY (`CourseID`),
  FOREIGN KEY (`TeacherID`) REFERENCES `Teacher`(`TeacherID`),
  FOREIGN KEY (`ClassID`) REFERENCES `Class`(`ClassID`)
);

CREATE TABLE IF NOT EXISTS `Schedule`(
	`ScheduleID` int NOT NULL AUTO_INCREMENT,
    `StartDate` dateTime,
    `EndDate` dateTime,
    `ScheduleStatus` enum('Proposed', 'Confirmed', 'Incomplete') DEFAULT 'Incomplete',
    `CourseID` int NOT NULL,
    `AdminID` VARCHAR(6),
    `EducationID` int NOT NULL,
    `CSID` VARCHAR(6),
    PRIMARY KEY (`ScheduleID`),
    FOREIGN KEY(`CourseID`) REFERENCES `Course`(`CourseID`),
    FOREIGN KEY(`AdminID`) REFERENCES `Admin`(`AdminID`),
    FOREIGN KEY(`EducationID`) REFERENCES `Education`(`EducationID`),
    FOREIGN KEY(`CSID`) REFERENCES `CourseSecretary`(`CSID`)
);

CREATE TABLE IF NOT EXISTS `Student`(
	`StudentID` VARCHAR(6),
    `UserID` int,
    `Enrollment` int NOT NULL,
    `CourseID` int NOT NULL,
    PRIMARY KEY (`StudentID`),
    FOREIGN KEY (`UserID`) REFERENCES `User`(`UserID`),
    FOREIGN KEY (`Enrollment`) REFERENCES `Education`(`EducationID`)
);

SELECT * FROM Location;
SELECT * FROM Course;
SELECT * FROM Class;
SELECT * FROM Schedule;
SELECT * FROM User;
SELECT * FROM Student;
SELECT * FROM Admin;
SELECT * FROM Teacher;
SELECT * FROM Education;
SELECT * FROM CourseSecretary;