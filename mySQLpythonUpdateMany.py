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
     with connection.cursor() as cursor:
         rows = [(10,'Bob'),
                 (92, 'MAC'),
                 (55, 'User')]
         cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",rows)        
         connection.commit()
# for row in cursor:
# print(row)
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()