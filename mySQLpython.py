import os
import datetime
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    # with connection.cursor() as cursor: <-- Displays as tupel
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
    # sql = "SELECT * FROM Employee;"
    # cursor.execute(sql)
    # cursor.execute(
    #     """CREATE TABLE IF NOT EXISTS 
    #     Friends(name char(20), age int, DOB datetime);"""
    #     )
        rows = [("Bob", 21, "1990-02-06 23:04:56"),
                ("MAC", 29, "1990-07-16 03:28:48"),
                ("User", 22, "2000-03-06 20:58:18")]
        cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
        connection.commit()
# for row in cursor:
# print(row)
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()