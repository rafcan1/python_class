'''
Exercise 110, file pp_110.py
Write a program that computes the value of n factorial - n!
Use RECURSIVE implementation
Expected results
-10! => ERROR
0! = 1
1! = 1
2! = 1 * 2 = 2
3! = 1 * 2 * 3 = 6
4! = 1 * 2 * 3 * 4
10! = 3628800
32! = 263130836933693530167218012160000000
n! = 1 * 2 * 3 * .... * n

'''

negative_num_error = -9999


def factorial(n):
    '''
    Functions calculates the factiorial of n

    Parameters:
        n: number, positive int
    Returns:
        The factorial or the error code

    '''
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return negative_num_error
    else:
        return n * factorial(n-1)


print(factorial(32))
