# INPUT OUTPUT OPERATIONS
"""
1.Command line: data can be entered on the command line when the program is invoked.
2.Keyboard input: a user can enter data when prompted by the program: input function
3.File input-output: a program can read data from or write data to files. We will focus on textual data.

PASSING COMMAND LINE ARGUMENTS

import sys #we need to import this if we are gonna use the system module
sys.argv-> is a list that contains the command-line arguments 
passed to a Python script when it's executed.



import sys

L1 = sys.argv

print(L1)  # we get the path, this list always has an element with the name of your file
# When we run the programme from the terminal, the file name is the first element in the list and
# whatever we write next to the file name in the command line is added to the list as a string

vowels = "aeiou"
word = sys.argv[1]
vowelcount = 0
for letter in word:
    if letter in vowels:
        vowelcount += 1
print(f'There are {vowelcount} vowels in this word')

import sys
vowels = "aeiou"
words = sys.argv[1:]
word_no = 0
for word in words:
    vowelcount = 0
    word_no += 1
    for letter in word:
        if letter in vowels:
            vowelcount += 1
    print(f'There are {vowelcount} vowels in this word no {word_no}')

"""


# FILE INPUT OUTPUT OPERATIONS

"""
1.Do not experiment with important files.
2.When you start working on your own files, make copies of them.
"""
# OPENING A FILE

"""
Opening a file:
open(file_path) -> method returns file object
example: 
outFile= open('testfile.txt','w')

Modes:
r->open a file for reading
w->open a file for writing.Creates a new file if it doesn't exist. Otherwise the content will be removed
a->opens a file to add into it without deleting the content. if file doesn't exist, it creates a new file
t->opens the file in text mode(default)
"""
# WRITING TO A FILE
"""
outFile = open('testfile.txt', 'a', encoding="utf-8")
outFile.write("and once more sometext'\n")
outFile.write("more text'\n")
outFile.close()
# after reading or writing we must close the file:
# outFile.close()
"""
# READING FROM A FILE
"""

"""
"""
inFile = open("testfile.txt", "r")
stuff = inFile.read()
lines = stuff.split("\n")  # will convert the entire string into a list
for line in lines:
    print(f'{line},:{len(line)}characters')
inFile.close()

inFile = open("testfile.txt", "r")
lines = inFile.readlines()  # will return the list of lines
for line in lines:
    print(f'{line},:{len(line)}characters')
inFile.close()
"""
# BETTER METHOD:
"""
inFile = open("testfile.txt", "r")
# will return the list of lines(better than the readlines method)
lines = inFile.read().splitlines()
for line in lines:
    print(f'{line},:{len(line)}characters')
inFile.close()
"""
"""
# WE DON'T HAVE TO CLOSE THE FILE THIS WAY:
with open("testfile.txt", "r") as inFile:
    lines = inFile.read().splitlines()
for line in lines:
    print(f'{line},:{len(line)}characters')


with open("testfile.txt", "w") as outFile:
    outFile.write("some text\n")

"""

try:
    a = int(input("Enter integer number \'a\':..."))
    b = int(input("Enter integer number \'b\':..."))
    num = a/b,
    print(f'The result of division {a} / {b} = {num}')
    print(f'writing the result to  the file...')
    with open("testfile.txt", "a", encoding="utf-8") as file:
        file.write(f'\nthe result of division {a}/ {b} = {num}')
except ValueError:
    print('You didn\'t enter the valid number')
except ZeroDivisionError:
    print('You can\'t divide by 0')
except FileNotFoundError:
    print('File doesn\'t exist')
except:
    print('Something went wrong!')
# Randint() is homework (read everything about this function, it will be invluded in the midterm)
