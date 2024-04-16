# NOT: READ TERNARY OPERATOR AT HOME


"""
############
EXCEPTIONS
############
*Exception is an error that terminates the execution of the program.
*It often happens due to programmer's mistake.
*it is our job to handle these exceptions and prevenet the application from crashing.

*Syntax error: print(7/3)) -> there is an extra parenthesis.
*Zero division error: print(2/0) -> numbers cannot be divided by zero
*Name error:local or global name cannot be found
*type error:operand doesn't have the correct type ("2"/"4")
*value error:value is illegal e.g. when you use int(input(".....")), user can use string
*index error: if index is out of range
*input-output error: IO system error e.g. file not found
*file not found error: similar to IO error
"""
"""
HANDLING EXCEPTIONS


try:
    numbers = [1, 2, 3]
    print(numbers[3])
except IndexError:
    print("Wrong Index!")
print("Here I am")

try:
    num = int(input("Enter number:.."))
    print(f'our number is {num}')
except ValueError:
    print('You didn\'t enter a valid number!')

try:
    a = int(input("Enter an integer number:"))
    b = int(input("Enter an integer number:"))
    num = a/b
except ValueError:
    print('You didn\'t enter a valid number!')
except ZeroDivisionError:
    print("You cannot divide a number by zero!")


RAISING EXCEPTIONS

*Giving conditions to handle errors.



def divide(a: int, b: int) -> float:
    """
# input: a,b positive int
# output: float
"""
    if a < 0 or b < 0:
        raise ValueError("You didn't enter a valid number")
    return a/b
"""


def get_positive_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            assert number >= 0, "Number should be greater than or equal to 0"
            return number
        except ValueError:
            print("invalid number entered")
        except AssertionError as error:
            print(error)


try:
    a = get_positive_int("Enter an integer number:")
    b = get_positive_int("Enter an integer number:")
    print(f'Division of a and b = {a/b}')
except ZeroDivisionError:
    print("Can't divide by 0")
except:
    # when we use multiple except expressions, we can use one without
    print("Sometinhg is wrong!")
    # giving the error type to handle any unexpected error typees and
    # we must put this except expression to the end of the other except statements
else:
    print("Code without exceptions")
    print(f'Multiplying a x b {a*b}.')
finally:
    print("the try..except block has been executed")
