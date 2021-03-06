SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS Location;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Schedule;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Admin;
DROP TABLE IF EXISTS Teacher;
DROP TABLE IF EXISTS CourseSecretary;
DROP TABLE IF EXISTS Education;
DROP TABLE IF EXISTS TimeFrame;
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
    `UserID` VARCHAR(6),
    PRIMARY KEY (`UserID`)
);

CREATE TABLE IF NOT EXISTS `Location`(
  `RoomID` VARCHAR(255) NOT NULL,
  `Address` VARCHAR(255),
  `LocationType` enum('Lecture hall','Classroom','Study hall','Study room') DEFAULT NULL,
  `Capacity` int DEFAULT NULL,
  PRIMARY KEY (`RoomID`)
);

CREATE TABLE IF NOT EXISTS `Teacher`(
    `TeacherID` VARCHAR(6),
    PRIMARY KEY (`TeacherID`),
    FOREIGN KEY (`TeacherID`) REFERENCES `User`(`UserID`)
);

CREATE TABLE IF NOT EXISTS `CourseSecretary`(
	`CSID` VARCHAR(6),
    PRIMARY KEY (`CSID`),
    FOREIGN KEY (`CSID`) REFERENCES `User`(`UserID`)
);

CREATE TABLE IF NOT EXISTS `Admin`(
	`AdminID` VARCHAR(6),
    PRIMARY KEY (`AdminID`),
    FOREIGN KEY (`AdminID`) REFERENCES `User`(`UserID`)
);

CREATE TABLE IF NOT EXISTS `Schedule`(
	`ScheduleID` int NOT NULL AUTO_INCREMENT,
    `StartDate` dateTime,
    `EndDate` dateTime,
    `ScheduleStatus` enum('Proposed', 'Confirmed', 'Incomplete') DEFAULT 'Incomplete',
    `AdminID` VARCHAR(6),
    `EducationID` int NOT NULL,
    `CSID` VARCHAR(6),
    PRIMARY KEY (`ScheduleID`),
    FOREIGN KEY(`AdminID`) REFERENCES `Admin`(`AdminID`),
    FOREIGN KEY(`EducationID`) REFERENCES `Education`(`EducationID`),
    FOREIGN KEY(`CSID`) REFERENCES `CourseSecretary`(`CSID`)
);

CREATE TABLE IF NOT EXISTS `Course`(
  `CourseID` VARCHAR(255),
  `ECTS` float DEFAULT NULL,
  `TeacherID` varchar(6) DEFAULT NULL,
  `Faculty` enum('SUND', 'HUM', 'JURA', 'Science', 'SAMF', 'TEOL', 'DTU'),
  `ScheduleID` int,
  PRIMARY KEY (`CourseID`),
  FOREIGN KEY (`TeacherID`) REFERENCES `Teacher`(`TeacherID`),
  FOREIGN KEY(`ScheduleID`) REFERENCES `Schedule`(`ScheduleID`)
);

CREATE TABLE IF NOT EXISTS `TimeFrame`(
  `TimeFrameID` int NOT NULL AUTO_INCREMENT,
  `StartTime` time DEFAULT NULL,
  `EndTime` time DEFAULT NULL,
  `Weekday`enum('Mon', 'Tue', 'Wed', 'Thu', 'Fri') not null,
  `CourseID` VARCHAR(255),
  `ClassType` enum('Lecture','Class','Meeting') DEFAULT NULL,
  `RoomID` VARCHAR(255),
  PRIMARY KEY (`TimeFrameID`),
  FOREIGN KEY (`RoomID`) REFERENCES `Location`(`RoomID`),
  FOREIGN KEY (`CourseID`) REFERENCES `Course`(`CourseID`)
);


CREATE TABLE IF NOT EXISTS `Student`(
	`StudentID` VARCHAR(6),
    `Enrollment` int NOT NULL,
    PRIMARY KEY (`StudentID`),
    FOREIGN KEY (`StudentID`) REFERENCES `User`(`UserID`),
    FOREIGN KEY (`Enrollment`) REFERENCES `Education`(`EducationID`)
);

SELECT * FROM Location;
SELECT * FROM Course;
SELECT * FROM TimeFrame;
SELECT * FROM Schedule;
SELECT * FROM User;
SELECT * FROM Student;
SELECT * FROM Admin;
SELECT * FROM Teacher;
SELECT * FROM Education;
SELECT * FROM CourseSecretary;