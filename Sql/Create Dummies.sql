INSERT into Education(EducationID, Title, University) Values (312, 'Sundhed og Informatik', 'KU');
INSERT into Education(EducationID, Title, University) Values (313, 'Folkesundhedsvidenskab', 'KU');
INSERT into Education(EducationID, Title, University) Values (311, 'Medicin og Teknologi', 'DTU');
INSERT into Education(EducationID, Title, University) Values (220, 'Religionsvidenskab', 'KU');
SELECT * From Education;

INSERT into User(FirstName, LastName, Mail, PhoneNumber, UserID) Values ('Susanne', 'Karlsen', 'SusanneKarlsen@hotmail.com', 12345678, 'ABC123');
INSERT into User(FirstName, LastName, Mail, PhoneNumber, UserID) Values ('Anders', 'Andersen', 'Anderandersen@gmail.com', 91011121, 'GWT352');
INSERT into User(FirstName, LastName, Mail, PhoneNumber, UserID) Values ('Julie', 'Jensen', 'JulieJensen@hotmail.com', 34567890, 'BCD234');
INSERT into User(FirstName, LastName, Mail, PhoneNumber, UserID) Values ('Hans', 'Hansen', 'Hanshansen@gmail.com', 13245376, 'FGH345');
INSERT into User(FirstName, LastName, Mail, PhoneNumber, UserID) Values ('Bent', 'Bentsen', 'Bent_bentsen@gmail.com', 11223344, 'ACD321');
INSERT into User(FirstName, LastName, Mail, PhoneNumber, UserID) Values ('Jan', 'Johanson', 'JJ@hotmail.com', 22334455, 'BDC987');
INSERT into User(FirstName, LastName, Mail, PhoneNumber, UserID) Values ('Peter', 'Petersen', 'PP@gmail.com', 20201020, 'JLM768');
INSERT into User(FirstName, LastName, Mail, PhoneNumber, UserID) Values ('Anna', 'Mortensen', 'A_Mortensen@hotmail.com', 33445566, 'UGI654');
INSERT into User(FirstName, LastName, Mail, PhoneNumber, UserID) Values ('Villy', 'Axelsen', 'Villy.Axelsen@gmail.com', 44556677, 'YTA175');
INSERT into User(FirstName, LastName, Mail, PhoneNumber, UserID) Values ('Ane', 'Petersen', 'AP@gmail.com', 55667788, 'JUM432');
INSERT into User(FirstName, LastName, Mail, PhoneNumber, UserID) Values ('Ole', 'Olsen', 'Oleolsen@gmail.com', 66778899, 'POT091');
INSERT into User(FirstName, LastName, Mail, PhoneNumber, UserID) Values ('Jeppe', 'Ipsen', 'J_ipsen@hotmail.com', 77889910, 'BTY667');
INSERT into User(FirstName, LastName, Mail, PhoneNumber, UserID) Values ('Lotte', 'Christensen', 'LotteC@gmail.com', 88991122, 'ABM552');
SELECT * FROM User;

INSERT into Location(RoomID, Address, LocationType, Capacity) Values ('A04', 'Universitetsparken 2', 'Lecture hall', 200);
INSERT into Location(RoomID, Address, LocationType, Capacity) Values ('UP1', 'Ole Maaløes Vej 5', 'Lecture hall', 150);
INSERT into Location(RoomID, Address, LocationType, Capacity) Values ('31.01', 'Blegdamsvej 3', 'Classroom', 50);
INSERT into Location(RoomID, Address, LocationType, Capacity) Values ('A01', 'Universitetsparken 2', 'Lecture hall', 240);
SELECT * FROM location;

INSERT into Teacher(TeacherID) Values ('ABC123');
INSERT into Teacher(TeacherID) Values ('ACD321');
INSERT into Teacher(TeacherID) Values ('BDC987');
INSERT into Teacher(TeacherID) Values ('JLM768');
SELECT * FROM Teacher;

INSERT into coursesecretary(CSID) Values('BCD234');
INSERT into coursesecretary(CSID) Values('UGI654');
INSERT into coursesecretary(CSID) Values('YTA175');
SELECT * FROM coursesecretary;

INSERT into admin(AdminID) Values('FGH345');
INSERT into admin(AdminID) Values('JUM432');
INSERT into admin(AdminID) Values('POT091');
SELECT * FROM admin;

INSERT into TimeFrame(TimeFrameID, StartTime, EndTime, Weekday, ClassType, RoomID) Values (NULL, '2022-05-20 08:00:00', '2022-05-20 10:00:00', 'Fri', 'Lecture', 'A04');
INSERT into TimeFrame(TimeFrameID, StartTime, EndTime, Weekday, ClassType, RoomID) Values (NULL, '2022-05-20 10:00:00', '2022-05-20 12:00:00', 'Fri', 'Class', '31.01');
INSERT into TimeFrame(TimeFrameID, StartTime, EndTime, Weekday, ClassType, RoomID) Values (NULL, '2022-05-23 13:00:00', '2022-05-20 17:00:00', 'Mon', 'Lecture', 'A01');
INSERT into TimeFrame(TimeFrameID, StartTime, EndTime, Weekday, ClassType, RoomID) Values (NULL, '2022-05-24 08:00:00', '2022-05-20 11:00:00', 'Tue', 'Lecture', 'UP1');
SELECT * FROM TimeFrame;

INSERT into course(CourseID, ECTS, TimeFrameID, TeacherID, Faculty) Values ('NDAB19000U', 7.5, 1, 'ABC123', 'Science');
INSERT into course(CourseID, ECTS, TimeFrameID, TeacherID, Faculty) Values ('SITB15002U', 10, 2, 'ACD321', 'SUND');
INSERT into course(CourseID, ECTS, TimeFrameID, TeacherID, Faculty) Values ('62560', 5, 3, 'BDC987', 'DTU');
INSERT into course(CourseID, ECTS, TimeFrameID, TeacherID, Faculty) Values ('SITB18009U', 7.5, 4, 'JLM768', 'SUND');
SELECT * FROM course;

INSERT into Schedule(ScheduleID, StartDate, EndDate, ScheduleStatus, CourseID, AdminID, EducationID, CSID) Values (NULL, '2022-02-01', '2022-07-01', 'Confirmed', 'NDAB19000U', 'FGH345', 312, 'BCD234');
INSERT into Schedule(ScheduleID, StartDate, EndDate, ScheduleStatus, CourseID, AdminID, EducationID, CSID) Values (NULL, '2022-02-01', '2022-07-01', 'Incomplete', 'SITB15002U', 'JUM432', 312, 'UGI654');
INSERT into Schedule(ScheduleID, StartDate, EndDate, ScheduleStatus, CourseID, AdminID, EducationID, CSID) Values (NULL, '2022-02-01', '2022-07-01', 'Proposed', 'SITB18009U', 'POT091', 312, 'YTA175');
SELECT * FROM schedule;

INSERT into student(StudentID, Enrollment, CourseID) Values ('GWT352', 312, 'NDAB19000U');
INSERT into student(StudentID, Enrollment, CourseID) Values ('BTY667', 312, 'NDAB19000U');
INSERT into student(StudentID, Enrollment, CourseID) Values ('ABM552', 312, 'NDAB19000U');
SELECT * FROM student;

SELECT user.userid, user.FirstName, user.LastName, user.mail, user.PhoneNumber, Teacher.TeacherID
FROM Teacher
LEFT OUTER JOIN USER
On Teacher.TeacherID = User.Userid;