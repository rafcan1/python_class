'''
Exercise 140, file pp_140.py

Variables are defined below:

sum = 3000
counter = 0

We want to divide sum by counter. 

Use the try... except... clause to handle a division by zero exception. 
If the division is done correctly, print the result to the console. At the time of error, let the following text be printed to the console: "You can't  divide by 0!"
'''

sum = 3000
counter = 0

try:
    print(sum / counter)
except ZeroDivisionError:
    print("You can't  divide by 0!")
