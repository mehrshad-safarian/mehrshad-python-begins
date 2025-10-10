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
    print(f"{item_to_check.capitalize()}is in the list.")
else:
    print(f"{item_to_check.capitalize()}is not in the list.")

# adding a new item to the list
new_item = input ("Enter a new item to add to the shopping list: ")
shopping_list.append(new_item)
print(f"Added {new_item} to the shopping list.")
print(shopping_list)