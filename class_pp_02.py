# LIST SORTING

# sort method mutates, sorts list in ascending order
"""
L1=[1,2,3,4,5]
L1.sort()

#sorted function creates a new object and doesn't mutate

"""

L1 = [
    ("Bread", 19),
    ("Butter", 20),
    ("Chocolate dark", 15),
    ("Chocolate white", 17),
    ("Cakes", 19)
]
"""
print(L1)
L1.sort(reverse=True)
print(L1)
"""
# list is sorted by the first element in the complex list
# What if we want to sort the list by the prices(second elements)?
# There is a "key" argument in this method.
# Below is how we can sort the list by the second element that has the index [1]
"""
def sort_product(item):
    return item[1]


L1.sort(key=sort_product)
print(L1)
"""
# LAMBDA FUNCTION

# A function that doesn't have a name
# it is useful when we need to use a function as a parameter like in the example above

# item is a parameter of this lambda function
L1.sort(key=lambda item: item[1])
print(L1)

# lambda function is usually a one-line function
