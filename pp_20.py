"""
Write a program that will raise all the elements of a list to third power
Input: list of integers
e.g., num=[1,2,3,4,5]
returns: list of integers raised to the third power
"""

L1 = [1, 2, 3, 4, 5]

L2 = list(map(lambda item: item**3, L1))
print(L2)
