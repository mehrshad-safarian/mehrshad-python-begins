# The print () function
print("Hellooo!")
print()
print("bye byyeee!!!")

# Using len
number00 = "789"
print(len(number00))

my_list = [7, 8, 4, 3, 2, 9]
print(len(my_list))

# Type conversion
number01 = "123"
integer = int(number01)
float_number = float(number01)

# mathematician operations
integer = 7
float_number = 13.1333
print(sum((integer, float_number)))

my_sum = sum((integer, float_number))
print(round(my_sum))

print(min(integer, float_number))
print(max(integer, float_number))

# Combining Functions 
numbers = []  # list to store the numbers

while True:
    user_input = input("Enter a number (type 'exit' to stop): ")
    
    if user_input.lower() == "exit":
        print("Exiting...")
        break

    try:
        number = float(user_input)
        numbers.append(number)  # add the number to the list
        print("You entered:", number)
    except ValueError:
        print("Invalid input! Please enter a number or type 'exit'.")

print("\nAll numbers you entered:")
print(numbers)  # this is a list
"""How the numbers were stored in a list
1. Create an empty list:
numbers = []
2. Every time the user enters a valid number, add it to the list using:
numbers.append(number)
Key points to remember
[] = list
() = tuple
.append() works only on lists (because lists are mutable)
Every append places the new value at the end of the list
In one sentence
We used numbers = [] to create a list, and each time a number was entered, numbers.append(number) added it to the list.
"""
average = sum(numbers) / len(numbers)
print(f"average of ur number's is :{average}")
rounded_avg_num = round(average)
print(f"Rounded avg og ur number is: {rounded_avg_num}")

# Using type()
mixed_list = [1, "three", 3.745, [9, 10]]
for item in mixed_list:
    print(f"The type of {item}, is{type(item)}")
    