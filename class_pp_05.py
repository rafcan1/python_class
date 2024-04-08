# words = ["data", "science", "machine", "learning"]
# word_length = {}
# for word in words:
#     word_lenght[word] = len(word)
# print(word_length)


# shakespeare text length analyzer
# work with chaining

# shakespeare = "When forty winters shall beseige thy brow, And dig deep trenches in thy beautys field, ...."
# shakespeare = shakespeare.replace(",", "").replace(".", "")
# words = shakespeare.split()
# word_length = {}
# for word in words:
#     word_length[word] = len(word)
# print(word_length)

# dictionary comprehension

# syntax:
# {item[0]:item[1] for item in iterable}
# {key: value for (key, value) in dict.items()}

# - for each item in items an expression is applied
# result: dictionary of key: value pairs

# words = ["data", "science", "machine", "learning"]
# word_length = {word: len(word) for word in words}
# print(word_length)


# shakespeare = "When forty winters shall beseige thy brow, And dig deep trenches in thy beautys field, ...."
# words = shakespeare.replace(",", "").replace(".", "").split()
# word_length = {word: len(word) for word in words}
# print(word_length)


# product_price_dic = {
#     "Bread" : 10,
#     "Butter" : 20,
#     "Chocolate dark" : 15,
#     "Chocolate white" : 17,
#     "Cakes" : 19
# }

# product_price_increased = {k: v*1.2 for k, v in product_price_dic.items()}
# print(product_price_increased)

# items_view = product_price_dic.items()
# for i in items_view:
# print(i)


# SORTING DICTIONARIES

# We can use sorted function to sort dictionaries but we must use item method

shakespeare = "When forty winters shall besiege thy brow, And dig deep trenches in the beautys field, ...."
words = shakespeare.replace(",", " ").replace(".", " ").split()
word_length = {word: len(word) for word in words}
sorted_word_length = sorted(
    word_length.items(), key=lambda item: item[1], reverse=True

)
print(sorted_word_length)
print(dict(sorted_word_length))
# We have converted a list of tuples into a dictionary using dict function
