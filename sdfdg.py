"""
articles = [
    {'id': 1, 'Name': 'Bike', 'Prod_Date': 2010, 'Price': 100},
    {'id': 2, 'Name': 'Bread', 'Prod_Date': 2022, 'Price': 5},
    {'id': 3, 'Name': 'Car', 'Prod_Date': 2017, 'Price': 5000},
    {'id': 4, 'Name': 'Bus', 'Prod_Date': 2007, 'Price': 1000},
]

filtered = list(filter(
    lambda item: item["Prod_Date"] > 2010 and item["Price"] > 1000, articles))

print(filtered)

net_price = [6.5, 3.4, 7.0, 9.1]
print([round(item * 1.23, 2) for item in net_price])
"""
items = ['P-1', 'A-2', 'D-6', 'Z-8']

print(list(map(lambda item: item.replace('-', ''), items)))
