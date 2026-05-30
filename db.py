import mysql.connector

def connect_db():

    conn = mysql.connector.connect(
        host="localhost",
        user="USERNAME",
        password="PASSWORD",
        database="DATABASE_NAME"
    )

    return conn
