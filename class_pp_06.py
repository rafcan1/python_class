# PASS STATEMENT

# Used as a placeholder for future code
"""
for i in range(1,5):
    pass
"""

# ESCAPE CHARACTERS

# is used to insert a special characters into a string. These symbols are normally illegal in python
# but we can use them for instance:
# a= "what's up"
# a= "what\'s up"

"""
\'	Single Quote
\\	Backslash
\n	New Line
\r	Carriage Return
\t	Tab
\b	Backspace
\f	Form Feed
\ooo	Octal value
\xhh	Hex value
"""
# print(r"C:\Users\Rafia\Documents\AMU\PYTHON CODE") or
# print("C:\\Users\\Rafia\\Documents\\AMU\\PYTHON CODE")
"""
# ITERABLES

# iterable is a container that stores multiple values
# it can be looped over: range objects, string,list,tuples,dictionaries...
"""
for i in range(5):
    print(i)

dic = {"a": 1, "b": 2, "c": 3, "d": 4}
for i in dic:
    print(i)

for i in dic.items():
    print(i)


d, c = (5, 6)  # We can unpack tuples like this:
print(d, c)

for k, v in dic.items():
    print(k, v)
"""
# DAC(divide and conquer) ALGORITHM
# recursively divide the problem into sub-problems, simpler problems, until it becomes simple enough to be
# solved directly

"""
"""
1.Divide: the problem into sub-problems
2.Conquer: Solve the sub-problems by calling recursively until solved
3.Combine:
"""

# RECURSION

"""
What is recursion?
A programming technique where a function calls itself
A recursive implementation is made up of two parts.
There is a base/termination condition that directly specifies the result for a special case.
There is at least one recursive case
"""


def f(n):
    """
    function prints all numbers from 0-n in a recursive way
    """
    f(n-1)
    print(n)


def f(n):
      """
    function prints all numbers from 0-n in a recursive way
    """

    if n>=0:
        f(n-1)
        print(n)

#MULTIPLE ITERATION EXAMPLE

def multi_iter(a,b):
     result=0

     while b>0:
          result+=a
return result