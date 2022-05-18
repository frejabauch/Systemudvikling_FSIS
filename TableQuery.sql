CREATE TABLE Teacher (
	name VARCHAR(255),
    contactinfo VARCHAR(255),
    courseaffiliations VARCHAR(255),
    userID int not null auto_increment,
    FOREIGN KEY (ScheduleID) references Schedule(ScheduleID),
    PRIMARY KEY (userID)
);

CREATE TABLE Schedule (
	ScheduleID int not null auto_increment,
    date datetime,
    status enum('Proposed', 'Confirmed', 'Incomplete'),
    PRIMARY KEY (ScheduleID)
);
