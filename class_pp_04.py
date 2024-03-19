# OTHER GIT COMMANDS
"""
git log: We can check the logs by using this command and see the commit id's
git checkout: moving between different commits(you temporarily load another state)
git revert: it revert creates a new commit with the changes that are rolled back. git reset erases your 
Git history instead of making a new commit.
"""
# FILTER FUNCTION
"""
filter(func,*iterables)
L1 = [1, 2, 4, 2, 9, 11, 12]


def filter_list(item):
    return item > 10

filtered_list = list(filter(filter_list, L1))
print(filtered_list)
"""


L1 = [
    ('Bread', 10),
    ('Butter', 20),
    ('Chocolate dark', 15),
    ('Chocolate white', 17),
    ('Cakes', 19)
]

# with this kind of 2D lists (or etc.) we need to give out the index of the elements
"""
filtered_list = list(filter(lambda item: item[1] > 15, L1))
print(filtered_list)

# FILTER FUNTION FOR LIST OF DICTIONARIES
articles = [
    {'id': 1, 'Name': 'Bike', 'Prod': 2010, 'Price': 100},
    {'id': 2, 'Name': 'Bread', 'Prod': 2022, 'Price': 5},
    {'id': 3, 'Name': 'Car', 'Prod': 2017, 'Price': 5000},
    {'id': 4, 'Name': 'Bus', 'Prod': 2007, 'Price': 1000},
]

filtered = list(filter(lambda item: item["Price"] > 100, articles))
print(filtered)
"""
# LIST REVISITED
"""
words =["data","science","machine","learning"]
word_length=[]
for word in words:
    word_length.append(len(word))
print(word_length)

#OR

word_length = list(map(lambda item: len(item),words))
print(word_length)
"""
# LIST COMPREHENSION
"""
When we make lists out of lists
[expression loop]
[expression for item in items]
"""
words = ["data", "science", "machine", "learning"]
word_length = [len(word) for word in words]
print(word_length)

L1 = [
    ('Bread', 10),
    ('Butter', 20),
    ('Chocolate dark', 15),
    ('Chocolate white', 17),
    ('Cakes', 19)
]
"""
prices = [item[1] for item in L1]
increased_prices = [item[1]*1.2 for item in L1]
product_prices = [(item[0], item[1]*1.2) for item in L1]
print(increased_prices, prices, product_prices)
"""
# We can use this syntax with if as well

max_prices = [(item[0], item[1]*1.2) for item in L1 if item[1] > 15]

print(max_prices)
