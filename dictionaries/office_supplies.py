inventory = {'item': 'printer paper', 'quantity': 587 , 'location': 'Storage Room C'}
inventory['quantity'] += 1700 
inventory['location'] += ' and Storage Room A also'
print("How many units of printer paper does the office have left, and where are they located?")
print(f"{inventory['quantity']}, units",inventory['location'])