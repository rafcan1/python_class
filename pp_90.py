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
    cleaned_text = ''.join(i.lower() for i in text if i.isalnum())
    start = 0
    end = len(cleaned_text) - 1

    while start < end:

        if cleaned_text[start] != cleaned_text[end]:
            return False
        start += 1
        end -= 1

    return True


# Test cases
palindromes = ["Dad", "Evil olive.", "Never odd or even.", "Amore, Roma."]
non_palindromes = ["test", "ad", "a", "'''"]

print("Palindromes:")
for palindrome in palindromes:
    print(f"{palindrome}: {is_palindrome(palindrome)}")

print("\nNon-palindromes:")
for non_palindrome in non_palindromes:
    print(f"{non_palindrome}: {is_palindrome(non_palindrome)}")
