#Install-MySQl-on-computer
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '0887123168'
    )

#prepare cursor object
cursorObject = dataBase.cursor()

#crate database
cursorObject.execute("CREATE DATABASE project1")
print('All Done!')
