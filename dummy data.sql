INSERT into Education(EducationID, Title, University) Values (312, 'Sundhed og Informatik', 'KU');
SELECT * From Education;

INSERT into User(FirstName, LastName, Mail, PhoneNumber, UserID) Values ('Susanne', 'Karlsen', 'SusanneKarlsen@hotmail.com', 12345678, NULL);
INSERT into User(FirstName, LastName, Mail, PhoneNumber, UserID) Values ('Anders', 'Andersen', 'Anderandersen@gmail.com', 91011121, NULL);
INSERT into User(FirstName, LastName, Mail, PhoneNumber, UserID) Values ('Julie', 'Jensen', 'JulieJensen@hotmail.com', 34567890, NULL);
INSERT into User(FirstName, LastName, Mail, PhoneNumber, UserID) Values ('Hans', 'Hansen', 'Hanshansen@gmail.com', 13245376, NULL);
SELECT * FROM User;

INSERT into Location(RoomID, Address, LocationType, Capacity) Values ('A04', 'Universitetsparken 2', 'Lecture hall', 200);
SELECT * FROM location;

INSERT into Teacher(TeacherID, UserID) Values ('ABC123', 1);
SELECT * FROM Teacher;

INSERT into coursesecretary(CSID, UserID) Values('BCD234', 3);
SELECT * FROM coursesecretary;

INSERT into admin(AdminID, UserID) Values('FGH345', 4);
SELECT * FROM admin;

INSERT into class(ClassID, StartTime, EndTime, ClassType, RoomID) Values (NULL, '2022-05-20 08:00:00', '2022-05-20 10:00:00', 'Lecture', 'A04');
SELECT * FROM class;

INSERT into course(CourseID, ECTS, ClassID, TeacherID, Faculty) Values ('NDAB19000U', 7.5, 1, 'ABC123', 'Science');
SELECT * FROM course;

INSERT into Schedule(ScheduleID, StartDate, EndDate, ScheduleStatus, CourseID, AdminID, EducationID, CSID) Values (NULL, '2022-02-01', '2022-07-01', 'Confirmed', 'NDAB19000U', 'FGH345', 312, 'BCD234');
SELECT * FROM schedule;

INSERT into student(StudentID, UserID, Enrollment, CourseID) Values ('GWT352', 2, 312, 'NDAB19000U');
SELECT * FROM student;

SELECT user.userid, user.FirstName, user.LastName, user.mail, user.PhoneNumber, Teacher.Teacherid
FROM Teacher
LEFT OUTER JOIN USER
On Teacher.Userid = User.Userid;