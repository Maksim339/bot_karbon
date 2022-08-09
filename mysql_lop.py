import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    password="",
    database="bot_karbon",
)

mycursor = mydb.cursor()
