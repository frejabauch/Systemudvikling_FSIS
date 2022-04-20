import classes

mette = classes.User("Mette", "g", "s", "Teacher")
proposeSchedule = classes.Teacher.proposeSchedule(["Mandag 12-14", "Tirsdag 10-17", "Onsdag 15-17", "Torsdag 8-15"])
print(proposeSchedule)