'''
Exercise 90, file pp_90.py
Write a program that will check if a word/sentence is a palindrome or not.
Remove punctuations and spaces
Use iterative way (loop) to check if palindrome

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


def is_palindrome(text: str) -> bool:
    '''
    Function checks if any text is palindrome or not

    Parameters:
        text: any text
    Returns:
        True: if text is palindrome
        False: if text is not a palindrome
    '''
    # your code below

    text = text.replace(" ", "").replace(".", "").replace(",", "").lower()
    mid = len(text)//2

    for i in range(mid):
        if text[i] != text[-i-1]:
            return False
    return True


my_text = input("Enter the word or sentence:...")
if is_palindrome(my_text):
    print(f'{my_text} : is a palindrome!!')
else:
    print(f'{my_text} : is not a palindrome!!')

# Test cases
palindromes = ["Dad", "Evil olive.", "Never odd or even.", "Amore, Roma."]
non_palindromes = ["test", "ad", "a", "'''"]
