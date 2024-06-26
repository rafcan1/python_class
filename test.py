"""
A list of words is given.

cities = ['Paris', 'Warsaw', 'New York']

Using the map () function and a lambda expression, convert the given list into a list containing the lengths of each word.
WRITE ONLY ONE LINE COMMAND, WITHOUT UNNECESSARY SPACES.
Expected result for : cities = ['Paris', 'Warsaw', 'New York']
[5, 6, 8]
Use parameter name: item
"""
"""
cities = ['Paris', 'Warsaw', 'New York']

city_length = list(map(lambda item: len(item), cities))
print(city_length)
"""
"""
Question
Using the sort () method and a lambda expression, sort, in a ascending way, the given list of dictionaries by the key 'Price'
WRITE ONLY ONE LINE COMMAND, WITHOUT UNNECESSARY SPACES.
Use parameter name: item
"""
"""
articles = [
    {'id': 1, 'Name': 'Bike', 'Prod': 2010, 'Price': 100},
    {'id': 2, 'Name': 'Bread', 'Prod': 2022, 'Price': 5},
    {'id': 3, 'Name': 'Car', 'Prod': 2017, 'Price': 5000},
    {'id': 4, 'Name': 'Bus', 'Prod': 2007, 'Price': 1000},
]
print(list(map(articles.sort(key=lambda item: item['Price']))))
"""

"""
Question:
in a descending way, according to the second element of the tuple object
WRITE ONLY ONE LINE COMMAND, WITHOUT UNNECESSARY SPACES.
for example :
pairs = [(3, 1), (7, 9), (4, 0), (8, 7)]
expected results:
[(7, 9), (8, 7), (3, 1), (4, 0)]
Use parameter name: item
"""
L1 = [4, 2, 6, 2, 11]
L2 = [5, 2, 3, 3, 9]
"""
The lists have the same length.
Using the map () function and a lambda expression, write a one-line-command which will transform the given lists into one (L3), containing the remainder of
dividing the element of the first list by the corresponding element of the second list.
Expected result of transformation:
[4, 0, 0, 2, 2]
"""
print(list(map(lambda item1, item2: item1 % item2, L1, L2)))
