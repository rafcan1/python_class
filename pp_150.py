'''
Exercise 150, file pp_150.py (on the basis of exercie 100)
Write a program that computes the value of n factorial - n!
Use iterative implementation
Expected results
0! = 1
1! = 1
2! = 1 * 2 = 2
3! = 1 * 2 * 3 = 6
4! = 1 * 2 * 3 * 4
10! = 3628800
32! = 263130836933693530167218012160000000
n! = 1 * 2 * 3 * .... * n

In order to do it implement the function 
def factorial(n: int) -> int:

Improve error handling using exceptions
'''


def factorial(n: int) -> int:
    '''
    Functions calculates the factiorial of n

    Parameters:
        n: number, positive int
    Returns:
        The factorial

    '''
    try:
        if n < 0:
            return -9999
        if n == 0 or n == 1:
            return 1
        num1 = 1
        for num in range(1, (n+1)):
            num1 = num1 * num

        return num1
    except ValueError:
        print("the number is not a positive number")


number = int(input("Enter a positive integer number:.."))
result = factorial(number)
message = "ERROR, You cant calculate factorial from negative number"
print(f'{number}! = {message if result == -9999 else result}')
