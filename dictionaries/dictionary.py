# dictionary in python 
# creating dictionaries

# person = {'name:' 'john', 'age:' '27' , 'city:' 'new york' } #incorrect
person = {'name' : 'gholi', 'age' : 199 , 'city' : 'New York'}

# Accessing dictionary values
print(f"name: {person['name']}")
print(f"age: {person['age']}")
print(f"city: {person['city']}")

# Adding and modifying dictionary values
person['email'] = 'gholi@example.com' #adding a new key-value pair
person['age'] = 33 # Modifying an existing value

# Removing dictionary item 
del person['city'] # Removing the 'city' key-value pair
age = person.pop('age') # Removing the 'age' key-value pair

# Iterating over dictioneries
for key in person:
    print(key, person[key]) # Iterating over keys and printing key-value pairs
# for value in person():  # incorrect
for value in person.values():
    print(value)  # Iterating over values
for key, value in person.items():
    print(key, value)  # Iterating over key-value pairs

# Dictionary methods
# keys()
# values()
# items()
# clear