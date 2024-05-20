r'''
Exercise 190

https://www.w3schools.com/python/python_regex.asp

Using RE find all the 5-characters length

Think about the following Special Sequences
\b
\w
{}


`\b` matches at the beginning or end of a word ². A word is defined as a sequence of alphanumeric characters or underscores, i.e., 
any character that can appear in a Python identifier ². The `\b` symbol is used to match word boundaries ¹. 

For example, in the string "The quick brown fox jumps over the lazy dog", `\bfox\b` would match "fox" but not "foxy" or "foxes" ¹.

'''
import re
import sys


def get_text(file_path: str, start_line: int) -> str:
    '''
    Function opens the text file and returns all 5-character long words

    Parameters:
        file_path: path to your text files
        start_line: text analysis should start at this specific line
    Returns:
        all words that have 5 characters in given text
    '''
    with open(file_path, "r") as file:
        lines = file.readlines()
        text = ''.join(lines[start_line-1:])
    result = re.findall(r"\b\w{5}\b", text, flags=0)
    return result


print(get_text("shakespeare.txt", 5))
