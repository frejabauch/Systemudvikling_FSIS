from Teacher import Teacher
from Schedule import Schedule
from TimeFrame import TimeFrame
import mysql.connector
from mysql.connector import errorcode

try:
    databaseConnector = mysql.connector.connect(user="root", password="Polythicml96.", host="127.0.0.1", database='new_Iter3')
    # databaseCursor = databaseConnector.cursor()
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Check username or password for database")

def loadTeacherFromDatabase(databaseConnector: mysql.connector.MySQLConnection, TeacherID: str) -> Teacher:
    databaseCursor = databaseConnector.cursor()
    query = f"SELECT FirstName, LastName, PhoneNumber, Mail FROM Teacher INNER JOIN User ON User.UserID=Teacher.TeacherID WHERE TeacherID='{TeacherID}'"
    databaseCursor.execute(query)
    result = databaseCursor.fetchall()
    return Teacher(*result[0])

proposingTeacher = loadTeacherFromDatabase(databaseConnector, "ABC123")

