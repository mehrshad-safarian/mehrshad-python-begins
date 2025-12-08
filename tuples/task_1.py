# review and run code to test if a string is to be found in another string
menu = "salad, pasta, sandwich, pizza, drinks, dessert"
print('Pizza' in menu)         # returns False
print('Pizza'.lower() in menu.lower()) # returns True

# review and run code to test case sensitive example
greeting = "Hello World"
print("'hello' in greeting = ", 'hello' in greeting) # returns False
print("'Hello' in greeting = ", 'Hello' in greeting) # returns True
print()

# example below: remove case sensitivity from a string comparison
# review and run code to test removing case sensitivity from a string comparison
print("'hello' in greeting.lower() = ", 'hello' in greeting.lower()) # returns True
print("'Hello' in greeting.lower() = ", 'Hello' in greeting.lower()) # returns False
print("'hello' in greeting if lower used = ", 'hello'.lower() in greeting.lower()) # returns True