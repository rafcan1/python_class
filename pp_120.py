'''
Exercise 120, file pp_120.py
Write a function that will check if a word/sentence is a palindrome or not.
Use recursive implementation
These are palindromes, test with them:
Dad 
Evil olive.
Never odd or even.
Amore, Roma.

Not palindromes:
test
ad
a
'''


def remove_punctuation(text: str, remove_space: bool = False) -> str:
    '''
    Function removes punctuations and optionally it can remove spaces

    Parameters:
        text: any text
        remove_space: if True, spaces are removed, if False, spaces are not removed
    Returns:
        text without punctuation, optionally spaces
    '''
    punctuation = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
    if text == "":
        return ""
    text = text.lower()
    if text[0] in punctuation:
        return remove_punctuation(text[1:], remove_space)
    else:
        if remove_space:
            if text[0] == " " and (text[-1] == " " or text[-1] in punctuation):
                return remove_punctuation(text[1:], remove_space)
            else:
                return text[0] + remove_punctuation(text[1:], remove_space)
        else:
            return text[0] + remove_punctuation(text[1:], remove_space)


def is_palindrome(text: str) -> bool:
    '''
    Function checks if any text is a palindrome

    Parameters:
        text: any text
    Returns:
        True: if text is palindrome
        False: if text is not a palindrome
    '''
    clean_text = remove_punctuation(text, remove_space=True)
    mid = len(clean_text)//2
    for i in range(mid):
        if clean_text[i] != clean_text[-i-1]:
            return False
    return True


def print_palindrome_check(text: str) -> None:
    '''
    Function prints the message if text is palindrome or not

    Parameters:
        text: any text
    '''

    my_text = input("Enter the word or sentence:...")
    if is_palindrome(my_text):
        print(f'{my_text} : is a palindrome!!')
    else:
        print(f'{my_text} : is not a palindrome!!')


print_palindrome_check("Never odd or even.")
