import mysql.connector
# print(dir(mysql))

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '123456'
    )

#  Prepare a cursor object
cursorObject = dataBase.cursor()

#  Create a database
cursorObject.execute("CREATE DATABASE elderco")
print("All Done!")