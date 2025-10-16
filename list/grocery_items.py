# nested list - gerocery items with quantities
gerocery_items = [
     ['milk', 2],
     ['potato', 7],
     ['apples', 3],
     ['pants', 2],
     ['banana', 5]
]

# accessing nested list items
print("Gerocery items with quantities: ")
for item, quantity in gerocery_items:
    print(f"{quantity} {item}{'\'s' if quantity > 1 else''}")


# modify the quantity of an item 
item_to_modify = input("Enter an item to modify its quantity: ")
item_found = False
for i, (item, quantity)  in enumerate(gerocery_items):
    if item == item_to_modify:
        new_quantity = int(input(f"Enter the new quantity for {item}:"))
        gerocery_items[i][1] = new_quantity
        item_found = True
        break
if item_found:
    print("Updated gerocery items with quantities:")
    for item , quantity in gerocery_items:
        print(f"{quantity} {item}{'s' if quantity > 1 else '' }")
else:
    print(f"{item_to_modify.capitalize()} is not in the gerocery list")
