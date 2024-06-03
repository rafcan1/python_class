'''
Exercise 230 (file pp_230.py)
Create a class (class TextIO) that will be responsible for reading text from file and writting text to file

Class data attributes:
filepath: str, file path of the file
start_line: int, the line number from which you start reading the file
_text:str, text that was read from file

Implement class procedural attributes:
def __init__(self, filepath, startline=0):
def get_text(self) -> str:
def read_from_file(self) -> None:
def write_to_file(self, text: str, f_path: str, mode: str = 'w') -> None:

Exception handling should be implemented

Enter filepath to read from file and startline using input() function
'''


class TextIO:
    def __init__(self, filepath, startline=0):
        self.filepath = filepath
        self.text = ""
        self.startline = startline

    def get_text(self) -> str:
        return self.text

    def read_from_file(self) -> None:
        with open(self.filepath, "r") as file:
            lines = file.readlines()
            ''.join(lines[self.startline:])

    def write_to_file(self, text: str, f_path: str, mode: str = "w") -> None:
        with open(f_path, mode) as file:
            file.write(text)


try:
    file_path = input("Enter file path to read from: ")
    startline = int(input("Enter the start line number (0-based index): "))

    text_io = TextIO(file_path, startline)
    text_io.read_from_file()
    print("Text read from file")

    file_path = input("Enter file path to write to: ")
    text_to_write = "Is it working now?"
    text_io.write_to_file(text_to_write, file_path)
    print(f"Text written to {file_path}.")

except ValueError:
    print("Please enter a number.")
except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
