import mysql.connector

def connect_db():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="B12vy1@2614",
        database="UMS"
    )

    return conn