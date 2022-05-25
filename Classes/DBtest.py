import datetime
import mysql.connector as mycn
from mysql.connector import errorcode

from Schedule import Schedule, ScheduleStatus

try:
    dbconn = mycn.connect(user="root", password="Polythicml96.", host="127.0.0.1", database='new_Iter3')

except mycn.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    else:
        print(f"{err.errno}")


cursor = dbconn.cursor()
#Eksempel på en SELECT query:
timeObject = datetime.datetime.now()

InputSchedule = Schedule(1234, timeObject, timeObject, ScheduleStatus.Confirmed, "NDAB19000U", "ABC123", 1234, "DEF456")

query = f"INSERT INTO Schedule(ScheduleID, StartDate, EndDate, ScheduleStatus, CourseID, AdminID, EducationID, CSID) VALUES ({InputSchedule.ScheduleID}, '{InputSchedule.StartDate}', '{InputSchedule.EndDate}', '{InputSchedule.ScheduleStatus.value}', '{InputSchedule.CourseID}', '{InputSchedule.AdminID}', {InputSchedule.EducationID}, '{InputSchedule.CSID}');"

cursor.execute(query)
# results = cursor.fetchall() #Fetches all rows
# #result = cursor.fetchone() Fetches first row of results
# for i in results:
#     print(i)
dbconn.commit()
cursor.close()
dbconn.close()