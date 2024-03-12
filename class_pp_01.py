# KEYWORD ARGUMENTS

# function(x=124,y=213234)(this one has keyword arguments) or function(124,213234)

# DEFAULT ARGUMENTS

# It is the argument that is used when you don't enter any arguments there

# def function(item_name, quantity=1): (default argument is quantity)

# *ARGS

#def print_numbers(*numbers): (prints a tuple)
#    print(numbers)

#def print_numbers(*numbers):  (the result will be printed as 1 number on each line)
#    for i in numbers:
#    print i

#print_numbers(1, 2, 3, 4, 5, "s")   (we can change the amount of arguments, we are more free)

# **KWARGS (like a place holder for dictionary items in the arguments section of a function)

# def add_user(**user):
#    print(user)

#add_user(id=1,name="John", surname="Kowalski") 
#we don't have to use "id" or "name", we can simply use ** when calling the function


# def print_user(--user: dict) -> None
#   for key,value in user.items():
#        print(f'{key} = {value}')


#LIST OF DICTIONARIES

# It is a good way of storing user info

# users = []

# def add_user(**user:dict) -> None:
#   users.append(user)

#add_user(id-1,Name="John", surname="Kowalski", Age=25)

# VARIABLE SCOPE

# We can access a variable from inside scope
# When we create a variable inside a funtion or a class, we cannot use it outside of the local scope.
#Variables inside the loops or if statements are still global variables

# message = "a"

#def my_func():
#   message = "b"
#   print(message)

#my_func()    (prints b) (local variable) (doesn't change the global variable)
#print(message) (prints a) (global variable)

#LIST UNPACKING

# Assigning variables into different elements of a list

# colors = ["red","yellow","green"]
# var1 = colors[0]
# var2 = colors[1]
# var3 = colors[2]

#numbers of the variables must be equal to the number of elements in the list

#numbers = [1,2,5,9,9,9,9,9,9,9]

# first_num, second_num, *others = numbers

#print(first_num)
#print(second_num)
#print(others)
