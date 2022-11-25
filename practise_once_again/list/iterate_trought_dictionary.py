a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
"""
#for key in a_dict:
    # print(key,':', a_dict[key])

d_items = a_dict.items()
print(d_items)

for item in a_dict.items():
    print(item)
    print(type(item))

for key, value in a_dict.items():
    print(f'{key}: {value}')

keys = a_dict.keys()
print(keys)

for key in a_dict.keys():
    print(key)

values = a_dict.values()
print(values)

for value in a_dict.values():
    print(value)

print('pet' in a_dict.keys())
print('apple' in a_dict.keys())
print('apple' in a_dict.values())

"""
"""

prices = {'apple': 0.40, 'orange': 0.35, 'banana':0.25}
for k, v in prices.items():
    prices[k] = round(v * 0.9, 2) # apply a 10% discount.

print(prices)

"""
"""

for key in list(prices.keys()): # Use a list instead of a view.
    if key == 'orange':
        del prices[key] # Delete a key from prices.

print(prices)

for key in prices.keys():
    if key == 'orange':
        del prices[key]

print(prices)

"""
"""

# Turning keys into value and vice versa.
a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {}
for key, value in a_dict.items():
    new_dict[value] = key

print(new_dict)

"""
"""

a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict ={} # Create a new empty dictionary
for key, value in a_dict.items():
    # If value satisfies the condition, then store it in a new_dict.
    if value <= 2:
        new_dict[key] = value

print(new_dicty)

"""
"""

incomes = { 'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
total_income = 0.00
for value in incomes.values():
    total_income += value # Accumulate the value in total_income

print(total_income)

"""
"""

# Using Comprehensions
objects = ['blue', 'apple', 'dog']
categories = ['color', 'fruit', 'pet']
a_dict = {key: value for key, value in zip(categories, objects)}
print(a_dict)

"""
"""

# Turning Keys into Values and Vice Versa:Revisited.
# Using dictionary_comprehension.
a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {value: key for key, value in a_dict.items()}
print(new_dict)
# Fitlering items: Revisited.
# Usidng dictionary_comprehension.
a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {k:v for k, v in a_dict.items() if v <= 2}
print(new_dict)
# Doing some calculations: Revisited
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
total_income = sum([value for value in incomes.values()])
print(total_income)
# Generator expression
total_income = sum(value for value in incomes.values())
print(total_income)
# Calculate incomes
total_income = sum(incomes.values())
print(total_income)

"""
"""

# Removing Specific Items.
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
non_citric = {k: incomes[k] for k in incomes.keys() - {'orange'}}
print(non_citric)
# Sorting a Dictionary.
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
sorted_income = {k: incomes[k] for k in sorted(incomes)}
print(sorted_income)
# Sorted by Keys.
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
for key in sorted(incomes):
    print(f'{key}: {incomes[key]}')
# Sorted by Values.

def by_value(item):
    return item[0]

for k, v in sorted(incomes.items(), key=by_value):
    print(k,": ", v)

for value in sorted(incomes.values()):
    print(value)

incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
for key in sorted(incomes, reverse=True):
    print(key, incomes[key])

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

while True:
    try:
        print(f'Dictionary length: {len(a_dict)}')
        item = a_dict.popitem()
        # Do something with item here...
        print(f'{item} removed')
    except KeyError:
        print('The dictionary has no item now...')
        break

prices_a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
prices_b = {'apple': 0.30, 'orange': 0.25, 'banana': 0.15}
def discount(current_price):
    return(current_price[0], round(current_price[1] * 0.95, 2))

new_prices_a = dict(map(discount, prices_a.items()))
new_price_b = dict(map(discount, prices_b.items()))
print(new_prices_a)
print(new_price_b)

prices_a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
def has_low_price(price):
    return prices_a[price] < 0.4

low_price = list(filter(has_low_price, prices_a.keys()))
print(low_price)


from collections import ChainMap
fruit_prices = {'apple': 0.40, 'orange': 0.35}
vegetable_prices = {'pepper': 0.20, 'onion':0.55}
chained_dict = ChainMap(fruit_prices, vegetable_prices)
print(chained_dict) # A ChainMap object.
for key in chained_dict:
    print(key, chained_dict[key])


from itertools import cycle
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
times = 3 # Define how many times you need to iterate through prices
total_items = times *len(prices)
for item in cycle(prices.items()):
    if not total_items:
        break
    total_items -= 1
    print(item)

"""

from itertools import chain
fruit_prices = {'apple': 0.40, 'orange': 0.35}
vegetable_prices = {'pepper': 0.20, 'onion':0.55}
for item in chain(fruit_prices.items(), vegetable_prices.items()):
    print(item)
