'''

Exercise 10, file pp_10.py
Write a function named fizz_buzz(num) that will return the string 'Fizz' if the num parameter  is divisible by 3,
will return the string 'Buzz' if the num is divisible by '5',
will return the string 'FizzBuzz' if the num is divisible by 3 and 5
will return num for any other number
Function should include docstring
Program should implement entering the number many times  during runtime. Typing "q"  should cause quitting the program.


'''


def fizz_buzz(num):
    """
    Returns 'Fizz' if num is divisible by 3,
    'Buzz' if num is divisible by 5,
    'FizzBuzz' if num is divisible by both 3 and 5,
    or the num itself for any other number.

    Args:
    - num: An integer input.

    Returns:
    - A string according to the FizzBuzz rules or the num itself.
    """
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)


while True:
    user_input = input("Enter a number or 'q' to quit: ")
    if user_input.lower() == 'q':
        print("Exiting the program.")
        break
    try:
        num = int(user_input)
        result = fizz_buzz(num)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a valid number or 'q' to quit.")
