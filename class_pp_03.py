# MAP FUNCTION

"""
It concerns using lambda functions in programs
map(func,*iterables)-> returns map object
func->lambda expression or pointer to a function 
which will be executed on each elements of the iterables
if you want to reach the elements of a map funtcion, turn it into a list
"""

L1 = [
    ("Bread", 10),
    ("Butter", 20),
    ("Chocolate dark", 15),
    ("Chocolate white", 17),
    ("Cakes", 19)
]
# We can pull the prices and create a list and put them inside the new list
# Here we did it by creating a function first and then used map func
"""
def get_item_1(item): 
    return item[1]


L2 = list(map(get_item_1, L1))
print(L2)
"""
# Below we use lambda function instead of creating a separate function as well.

L2 = list(map(lambda item: item[1], L1))
print(L2)

# Below we create a list that contains the products and the prices, prices are increased by 20%

L3 = list(map(lambda item: (item[0], item[1]*1.2), L1))
print(L3)
