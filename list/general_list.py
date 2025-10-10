# Lists in Python
# Creating Lists
fruits = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mixed = ['hello', 9, True, [1, 2]]

# Accessing List Elements
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[-1])  # Output: cherry

# List Slicing list. The syntax is [start:stop:step]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:6])  # Output: [3, 4, 5, 6]
print(numbers[:4])  # Output: [1, 2, 3, 4] (from start)
print(numbers[4:])  # Output: [5, 6, 7, 8, 9] (to the end)
print(numbers[::2])  # Output: [1, 3, 5, 7, 9] (every other element)

# List Operations
vegetables = ['carrot', 'potato']
combined = fruits + vegetables  # Concatenation
print(combined)  # Output: ['apple', 'banana', 'cherry', 'carrot', 'potato']

repeated = 2 * fruits  # Repetition
print(repeated)   # Output: ['apple', 'banana', 'cherry', 'apple', 'banana', 'cherry']

print('banana' in fruits)  # Membership testing, Output: True
print('orange' in fruits)  # Membership testing, Output: False

# List Methods
print(fruits)
fruits.append('orange')  # Appends an element to the end
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

fruits.insert(1,'grape') # Inserts an element at a specific index
print(fruits)  # Output: ['apple', 'grape', 'banana', 'cherry', 'orange']

fruits.remove('banana')  # Removes the first occurrence of an element
print(fruits)  # Output: ['apple', 'grape', 'cherry', 'orange']

fruits.pop(1)  # Removes and returns the element at a specific index
print(fruits)  # Output: ['apple', 'cherry', 'orange']

fruits.sort()  # Sorts the list in place
print(fruits)  # Output: ['apple', 'cherry', 'orange']

# List of grades
grades = [85, 92, 77, 88, 95]

# Trying to access an invalid index
try:
    print(grades[10])  # Raises IndexError
except IndexError:
    print("Invalid index, list out of bounds!")

# Assigning a value to an invalid index

try:
    grades[10]=90  # Raise IndexError
except IndexError:
    print("Cannot assign to an index outside the list!")

# Nesting Lists
# List of students
students = [
    ['John', [85, 92, 88]],
    ['Emma', [77, 89, 94]],
    ['Michel', [65, 72, 81]],
    ['Sophia', [92, 88, 95]]
]

# Accessing a student's name
print(students[2][0])  # Output: Michael

# Accessing a student's grades
print(students[1][1])  # Output: [77, 89, 94]

# Modifying students' grades
students[0][1][1] = 95  # Update John's second grade to 95

# A 3x4 matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Accessing the elements
print(matrix[1][2])  # Output: 7

# Modifying an element
matrix[0][0] = 100
print(matrix[0][0])