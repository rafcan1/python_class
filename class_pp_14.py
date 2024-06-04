# WORKING WITH A DATABASE USING PYTHON AND SQLite

"""
Relational tables
*have tuples
*no duplicate rows
*columns have unique names
*each column has a data type
*all rows has have the same set of tables
*We can set "primary key" (PK) to certain columns e.g. ID: then all IDs will be unique
*NN(not null) means we cannot leave those column empty like name and surname

"""
"""
SQL 
some SQL commands:

INSERT INTO table_name (column1, column2...)
VALUES (value1, value2 ...);

#If you are adding value for all of the columns, no need to specify the column names

INSERT INTO table_name
VALUES (value1, value2....);

SELECT column1, column2,...  #selects the chosen columns
FROM table_name;

SELECT *FROM table_name #all the fields available from the table

SELECT column1
FROM  table_name
WHERE condition;   #used to filter the records

Python + SQL
We used the pp_database.py file 
"""

"""
connection = sqlite3.connect(
    r'C:\\Users\\Rafia\\Documents\\AMU\\PYTHON CODE\\PYTHON PROGRAMMING\\MyDB.db')
command = "INSERT INTO Clients (Id, Name, Surname) VALUES (2, 'Tim', 'Jones')"
connection.execute(command)
connection.commit()  # all changes are written to the database
connection.close()  # always close the resource
"""
# better way:
# with sqlite3.connect(r'C:\\Users\\Rafia\\Documents\\AMU\\PYTHON CODE\\PYTHON PROGRAMMING\\MyDB.db') as conn:
import sqlite3
 # command = "INSERT INTO Clients (Id, Name, Surname) VALUES (3, 'Tim', 'Jones')"
# conn.execute(command)
"""
L1 = [
    ('Jessica', 'Jones', 'IT', 2020),
    ('Super', 'Man', 'Heroes', 2018),
    ('Wonder', 'Woman', 'Heroes', 2021),
]
with sqlite3.connect(r'C:\\Users\\Rafia\\Documents\\AMU\\PYTHON CODE\\PYTHON PROGRAMMING\\MyDB.db') as conn:
    #     # "?" are placeholders for the values you are going to supply in the next step
    command = "INSERT INTO Students (Name, Surname, Major, AdmissionYear)  VALUES(?,?,?,?)"
    for l in L1:
        conn.execute(command, l)
"""
"""
READING FROM DATABASE

with sqlite3.connect(r'C:\\Users\\Rafia\\Documents\\AMU\\PYTHON CODE\\PYTHON PROGRAMMING\\MyDB.db') as conn:
    command = "SELECT * FROM Students"
    cursor = conn.execute(command)  # cursor is an iterable object
    for row in cursor:
        print(row)

with sqlite3.connect(r'C:\\Users\\Rafia\\Documents\\AMU\\PYTHON CODE\\PYTHON PROGRAMMING\\MyDB.db') as conn:
    command = "SELECT * FROM Students WHERE Name = 'Jessica'"
    cursor = conn.execute(command)  # cursor is an iterable object
    for row in cursor:
        print(row)
"""
