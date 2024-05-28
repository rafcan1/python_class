r'''
Programming Task 03 (file pt_03.py)
Points: 15

https://www.w3schools.com/python/python_regex.asp

On the basis of Exercise 190,
Using RE, in 'shakespeare.txt' file, find and print all the 6-characters length words which starts with a vowel and ends with a consonant.
Additionally, print the amount of these words.
Vowels: 'aeoiuy'
Consonants: 'bcdfghjklmnpqrstvwz'
Think about the following Special Sequences
\b
\w
{}

Start your analysis from the line no 254.

`\b` matches at the beginning or end of a word ². A word is defined as a sequence of alphanumeric characters or underscores, i.e., 
any character that can appear in a Python identifier ². The `\b` symbol is used to match word boundaries ¹. 

For example, in the string "The quick brown fox jumps over the lazy dog", `\bfox\b` would match "fox" but not "foxy" or "foxes" ¹.
Use input function to enter the line no, from which you start your analysis

Implement the exception handling: FileNotFoundError, ValueError

Exemplary start 
###############################################
Text analyzer - finds all 6 characters length words
which starts with a vowel and ends with a consonant

Enter the line number from which you want to start analysis: 254

Results:
['eating' ...]
The amount of words is 341

'''
import re
import sys


def get_text(file_path: str, start_line: int) -> str:
    '''
    Function opens the text file and returns its content

    Parameters:
        file_path: path to your text file
        start_line: text analysis should start at this specific line
    Returns:
        text
    '''

    with open(file_path, "r") as file:
        lines = file.readlines()
        text = ''.join(lines[start_line-1:])
        return text


def text_analyzer(file: str):
    """
    Text analyzer - finds all 6 characters length words
    which starts with a vowel and ends with a consonant

    """
    result = re.findall(r'[\w.-]+@[\w.-]+', file)
    #   r"\b[aeiouyAEIOUY]\w{4}[bcdfghjklmnpqrstvwzBCDFGHJKLMNPQRSTVWZ]\b", file, flags=0)

    amount = len(result)
    string = f'The amount of words is {amount}.'
    print(result)
    print(string)


try:
    file = r"c:/Users/Rafia/Documents/AMU/PYTHON CODE/PYTHON PROGRAMMING/shakespeare.txt"
    print("###############################################")
    print("Text analyzer - finds all 6 characters length words which starts with a vowel and ends with a consonant")
    answer = int(input("Enter the number of the line: "))
    text_analyzer(get_text(file, answer))

except FileNotFoundError:
    print("The specified file was not found.")
except ValueError:
    print("Please enter a positive number.")

# FEEDBACK OF PT 03:
# don't add exception handling inside your functions.
# Exception handling must be handled at the outermost level.
