'''
Exercise 240, file pp_240.py

Using your knowledge from previous exercises

Your task is, using python:
0. Entering text_file_path, db_file_path, start_line
1. Create a MyDB01.db (everything using python) Create a table Alice_tb with columns Id integer primary key, Line text, Length integer
2. Read text data from alice.txt (use your TextIO class from your module)
3. Analize your text:
- lines_length data structure variable
- save your data in lines_length variable
- write your data to DB
3. Read first 10 data rows from your database and print to the terminal

In order to do the exercise, implement the following functions:
def get_lines_length(text: str) -> list[tuple[str, int]]:
def write_alice_tb(db_file_path: str, data: list[tuple[str, int]]) -> None:
def read_alice_tb(db_file_path: str) -> list[tuple[int, str, int]]:
def print_alice_tb(data: list[tuple[int, str, int]], number: int) -> None:

'''
import sqlite3
from texta import TextIO


def get_lines_length(text: str) -> list[tuple[str, int]]:
    lines = text.split("\n")
    result = [(line, len(line)) for line in lines]
    return result


def write_alice_tb(db_file_path: str, data: list[tuple[str, int]]) -> None:
    with sqlite3.connect(db_file_path) as conn:
        conn.execute(
            '''CREATE TABLE IF NOT EXISTS Alice_tb
         (Id INTEGER PRIMARY KEY,
         Line TEXT,
         Length INTEGER)''')
        command = "INSERT INTO Alice_tb (Id, Line, Length)  VALUES(?,?,?)"
        data = [(i+1, *t)for i, t in enumerate(data)]
        for l in data:
            conn.execute(command, l)


def read_alice_tb(db_file_path: str) -> list[tuple[int, str, int]]:
    with sqlite3.connect(db_file_path) as conn:
        command = "SELECT * FROM Alice_tb"
        cursor = conn.execute(command)  # cursor is an iterable object
        list = []
        for row in cursor:
            list.append(row)
        return list


def print_alice_tb(data: list[tuple[int, str, int]], number: int) -> None:
    for i in range(min(number, len(data))):
        print(data[i])


file = r'C:\\Users\\Rafia\\Documents\\AMU\\PYTHON CODE\\PYTHON PROGRAMMING\\alice.txt'
try:
    s_line = int(
        input('Enter the line number from which you want to start analysis: '))

    tio = TextIO(file, s_line)
    tio.read_from_file()
    all_text = tio.get_text()
    lines_length = get_lines_length(all_text)
    database_file_path = input("Enter the file path for your database: ")
    # write_alice_tb(database_file_path, lines_length)
    meow = read_alice_tb(database_file_path)
    print_alice_tb(meow, 10)
except ValueError as err:
    print(f"You entered wrong line number, {err}")
except FileNotFoundError as err:
    print(err)
except Exception as err:
    print(err)
