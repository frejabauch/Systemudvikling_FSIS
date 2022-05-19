import mysql.connector as mycn
from mysql.connector import errorcode

try:
    dbconn = mycn.connect(user="root", password="password her", host="127.0.0.1", database='databasenavn her')
    cursor = dbconn.cursor()
    #Eksempel på en SELECT query:
    query = r"SELECT ScheduleID, TIME_FORMAT(StartTime, '%H:%i'), TIME_FORMAT(EndTime, '%H:%i') FROM TimeFrame WHERE ScheduleID=1;" #Selection query

    cursor.execute(query)
    results = cursor.fetchall() #Fetches all rows
    #result = cursor.fetchone() Fetches first row of results
    for i in results:
        print(i)

except mycn.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
else:
    # print("Reached else statement")
    cursor.close()
    dbconn.close()