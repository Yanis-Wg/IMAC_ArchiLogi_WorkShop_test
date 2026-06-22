import mysql.connector

def connectToDB() :
    myDb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ryj"
    )

    return myDb