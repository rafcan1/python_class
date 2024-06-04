'''
---------------------------------------------
WORKING WITH A DATABASE USING PYTHON
and DB SQLite
---------------------------------------------
'''

# # 1.0 Inserting data into database :
# connection = sqlite3.connect(r'PYTHON PROGRAMMING\MyDB.db')
# command = "INSERT INTO Clients (Id, Name, Surname) VALUES (1, 'Tim', 'Jones')"
# connection.execute(command)
# connection.commit()  # all changes are written to the database
# connection.close()  # always close the resource


# # # 1.01 Inserting data into database
# # # Better way
# with sqlite3.connect(r'PYTHON PROGRAMMING\MyDB.db') as conn:
#     command = "INSERT INTO Clients (Id, Name, Surname) VALUES (1, 'Tim', 'Jones')"
#     conn.execute(command)

# # 1.02 Inserting data into database
# #

# L1 = [
#     ('Jessica', 'Jones', 'IT', 2020),
#     ('Super', 'Man', 'Heroes', 2018),
#     ('Wonder', 'Woman', 'Heroes', 2021),
# ]

# with sqlite3.connect(r'PYTHON PROGRAMMING\MyDB.db') as conn:
#     # "?" are placeholders for the values you are going to supply in the next step
#     command = "INSERT INTO Students (Name, Surname, Major, AdmissionYear)  VALUES(?,?,?,?)"
#     for l in L1:
#         conn.execute(command, l)

################################################################################################################

# # 2. Reading data from database
# #

# with sqlite3.connect(r'PYTHON PROGRAMMING\MyDB.db') as conn:
#     command = "SELECT * FROM Students"
#     cursor = conn.execute(command)  # cursor is an iterable object
#     for row in cursor:
#         print(row)

# # # 2.01 Reading data from database
# # #
# with sqlite3.connect(r'PYTHON PROGRAMMING\MyDB.db') as conn:
#     command = "SELECT * FROM Students"
#     cursor = conn.execute(command)  # cursor is an iterable object
#     students = cursor.fetchall()  # returns all the rows in the table in one go
#     print(students)

# # # 3. Reading data from database, WHERE clause
# # #

# with sqlite3.connect(r'PYTHON PROGRAMMING\MyDB.db') as conn:
#     command = "SELECT * FROM Students WHERE Name = 'Jessica'"
#     cursor = conn.execute(command)  # cursor is an iterable object
#     for row in cursor:
#         print(row)

# # # 3.1 Reading data from database, WHERE clause
# # #

# with sqlite3.connect(r'PYTHON PROGRAMMING\MyDB.db') as conn:
#     command = "SELECT Name, Surname FROM Students WHERE AdmissionYear = 2020"
#     cursor = conn.execute(command)  # cursor is an iterable object
#     for row in cursor:
#         print(row)

# # # PROJECT FROM THE BEGINNING
# # # 4.0 Creating database and tables
# L1 = [
#     ('Jessica', 'Jones', 'IT', 2020),
#     ('Super', 'Man', 'Heroes', 2018),
#     ('Wonder', 'Woman', 'Heroes', 2021),
# ]

# with sqlite3.connect(r'PYTHON PROGRAMMING\MyDB.db') as conn:
#     conn.execute(
#         "CREATE TABLE IF NOT EXISTS Students ('Id' INTEGER, 'Name' TEXT, 'Surname' TEXT, 'Major' TEXT, 'AdmissionYear' INTEGER)")
#     command = "INSERT INTO Students (Name, Surname, Major, AdmissionYear)  VALUES(?,?,?,?)"
#     for l in L1:
#         conn.execute(command, l)


# # # 4.1 Creating database and tables
# L1 = [
#     ('Jessica', 'Jones', 'IT', 2020),
#     ('Super', 'Man', 'Heroes', 2018),
#     ('Wonder', 'Woman', 'Heroes', 2021),
# ]

# with sqlite3.connect(r'PYTHON PROGRAMMING\MyDB.db') as conn:
#     conn.execute(
#         '''CREATE TABLE IF NOT EXISTS Students
#         (Id INTEGER PRIMARY KEY,
#         Name TEXT NOT NULL,
#         Surname TEXT NOT NULL,
#         Major TEXT,
#         AdmissionYear INTEGER)''')
#     command = "INSERT INTO Students (Name, Surname, Major, AdmissionYear)  VALUES(?,?,?,?)"
#     for l in L1:
#         conn.execute(command, l)
