"""
A program that lists 4 items sold at a cafe
Using dictionaries for stock and price then calculate total stock worth
"""

menu = ["sandwich", "soup", "salad", "fries"]

stock = {'sandwich': 10, 
         'soup': 15, 
         'salad': 10, 
         'fries': 15}

price = {'sandwich': 6, 
          'soup': 8, 
          'salad': 8, 
          'fries': 4}

# Calculate total by looping stock multiplied by price per index
total = 0
for food in menu:
    total += stock[food] * price[food]

print(f"The total stock worth is: £{total}")

