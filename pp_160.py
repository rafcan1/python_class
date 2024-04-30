'''
Exercise 160, pp_160.py

Task is the same as in exercise 40 - finding the longest word in the given text, but additionally you have to implement a function get_text().
The new function should return the text from a file,
Write a program with a function called map_longest() that takes a text as a parameter and returns the longest word contained in that text and its length - tuple.

Result of a program should be a message
e.g. after punctuation removal
The longest word in the file 'shakespeare.txt' is 'internethartvmdcsouiucedu' with the length of 25 characters

e.g. without punctuation removal
The longest word in the file 'shakespeare.txt' is '>internet:hart@.vmd.cso.uiuc.edu' with the length of 32 characters

use map function together with lambda

Exception handling should be implemented.
Implement the possibility of entering file_path from command line
'''


def get_text(file_path: str) -> str:
    '''
    Function opens the text file and returns its content

    Parameters:
        file_path: path to your text file
    Returns:
        text
    '''
    try:
        with open(file_path, "r", encoding="utf-8") as inFile:
            return inFile.read()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except:
        print("Error")


def remove_punctuation(word: str) -> str:
    '''
    Function removes punctuation from the given string

    Parameters:
        word: any string with or without the punctuation
    Returns:
        string without punctuation
    '''
    punc = '''!()-[]{,};:'"\n\\,<<>>./?@#$%^&*_~'''

    def remover(word): return ''.join(
        map(lambda char: '' if char in punc else char, word))
    return remover


def map_longest(text: str) -> tuple:
    '''
    Function returns the longest word in the text and it's length

    Parameters:
        text: any text

    Returns:
        tuple: a tuple containing the longest word and it's length

    '''
    my_text = text.split()
    result = list(map(lambda item: (len(item), item), my_text))
    sorted_text = sorted(result, reverse=True)
    longest = sorted_text[0]
    text = (
        f'The longest word in the file is {longest[1]} with the length of {longest[0]} characters')
    return text


print(map_longest(remove_punctuation(get_text("shakespeare.txt"))))
