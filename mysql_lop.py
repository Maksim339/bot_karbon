import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    password="05061MaKsIm!",
    database="bot_karbon",
)

mycursor = mydb.cursor()