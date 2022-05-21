USE Iteration3;

CREATE TABLE Schedule (
	ScheduleID int not null auto_increment,
    StartDate date,
    EndDate date,
    status enum('Proposed', 'Confirmed', 'Incomplete') DEFAULT 'Incomplete',
    PRIMARY KEY (ScheduleID)
);

CREATE TABLE Teacher (
	name VARCHAR(255),
    contactinfo VARCHAR(255),
    courseaffiliations VARCHAR(255),
    userID int not null auto_increment,
    ScheduleID int,
    FOREIGN KEY (ScheduleID) references Schedule(ScheduleID),
    PRIMARY KEY (userID)
);

CREATE TABLE Location (
  RoomID int NOT NULL AUTO_INCREMENT,
  Address text,
  Location_Type enum('Lecture hall', 'classroom', 'studyhall', 'studyroom') DEFAULT NULL,
  Capacity int DEFAULT NULL,
  RoomSchedule text,
  PRIMARY KEY (RoomID)
);


CREATE TABLE Class (
  ClassID int NOT NULL AUTO_INCREMENT,
  Time datetime DEFAULT NULL,
  ClassType enum('Lecture', 'class', 'meeting') DEFAULT NULL,
  Student_list text,
  TeacherID text,
  RoomID int DEFAULT NULL,
  PRIMARY KEY (ClassID),
  KEY RoomID (RoomID),
  CONSTRAINT class_ibfk_1 FOREIGN KEY (RoomID) REFERENCES Location (RoomID)
);

CREATE TABLE Courses (
  CourseID int NOT NULL AUTO_INCREMENT,
  ScheduleID int,
  ECTS float DEFAULT NULL,
  Student_list text,
  TeacherID varchar(50) DEFAULT NULL,
  Location varchar(50) DEFAULT NULL,
  PRIMARY KEY (CourseID),
  FOREIGN KEY (ScheduleID) references Schedule(ScheduleID)
);

CREATE TABLE TimeFrame (
	ScheduleID int,
    StartTime time,
    EndTime time,
    Weekday enum('Man', 'Tirs', 'Ons', 'Tors', 'Fre') not null,
    FOREIGN KEY (ScheduleID) references Schedule(ScheduleID)
);
