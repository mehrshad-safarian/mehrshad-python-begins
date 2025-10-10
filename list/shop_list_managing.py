# checking if an item in the list
# adding an item to the list
# removing an item from the list
# accessing an item by index
# modifying the quantity of an item in the nested grocery list


# shopping list
shopping_list = ['milk', 'eggs', 'bread', 'cheese', 'apples']

#print the list 
print("shopping list:")
print(shopping_list)

# checking if an item in the list
item_to_check = input("Enter an item to check if it's in the shopping list:")
if item_to_check in shopping_list:
    print(f"{item_to_check.capitalize()} is in the list.")
else:
    print(f"{item_to_check.capitalize()} is not in the list.")

# adding a new item to the list
new_item = input ("Enter a new item to add to the shopping list: ")
shopping_list.append(new_item)
print(f"Added {new_item} to the shopping list.")
print(shopping_list)

# removing an item from the list
item_to_remove = input("Enter an item to remove from the list :")
if item_to_remove in shopping_list:
    shopping_list.remove(item_to_remove)
    print(f"Removed {item_to_remove.capitalize()} from the shopping list")
else:
    print(f"{item_to_remove.capitalize()} is not in the list")
    print(shopping_list)


# while True:
#     # Ask the user to enter an item to remove
#     item_to_remove = input("Enter an item to remove from the list: ").lower()

#     # Keep asking until the user enters an item that exists in the list
#     while item_to_remove not in shopping_list:
#         print(f"{item_to_remove.capitalize()} is not in the list.")
#         print("Current shopping list:", shopping_list)
#         item_to_remove = input("Please enter a valid item to remove: ").lower()

#     # Remove the item and show confirmation
#     shopping_list.remove(item_to_remove)
#     print(f"Removed {item_to_remove.capitalize()} from the shopping list")
#     print("Current shopping list:", shopping_list)

#     # Ask if the user wants to remove another item
#     another = input("Do you want to remove another item? (yes/no): ").lower()

#     # Exit the program if the user types anything other than "yes"
#     if another != "yes":
#         print("Exiting program...")
#         break

# sort the list alphabetically
shopping_list.sort()
print("shopping list sorted alphabetically:")
print(shopping_list)

# accessing an item
index = int(input("Pls enter an index to access an the item in the list: "))
try:
    print(f"the item at index {index} is {shopping_list[index]}")
except IndexError:
    print("invalid index, list out of bounds!")

