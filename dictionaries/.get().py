it_inventory = {
    "LAP001": {
        "type": "Laptop",
        "model": "ThinkPad X1",
        "status": "In Use",
        "assigned_to": "Sarah Chen",
        "department": "Development",
        "location": "Floor 2",
        "purchase_info": {
            "date": "2023-05-15",
            "cost": 1299.99,
            "supplier": "TechVendor Inc"
        },
        "maintenance": {
            "last_check": "2024-01-10",
            "next_check": "2024-04-10",
            "condition": "Excellent"
        }
    },
    "MON002": {
        "type": "Monitor",
        "model": "Dell U2419H",
        "status": "Available",
        "location": "Storage Room",
        "purchase_info": {
            "date": "2023-06-20",
            "cost": 249.99,
            "supplier": "Office Solutions Ltd"
        },
        "maintenance": {
            "last_check": "2024-01-15",
            "next_check": "2024-04-15",
            "condition": "Good"
        }
    }
}
# getting something that doesn’t exist:
printer_status = it_inventory.get("PRN001","Not Found!")
print(printer_status)
# "PRN001" key does not exist in the dictionary.
# So .get() returns the second argument "Not Found".

# getting something that does exists
laptop_status = it_inventory.get("LAP001", "Not Found!")
print(laptop_status)
# key exists, so Python returns its whole value 
# which is another dictionary with all the laptop info.

# using .get() with an empty dictionary {} as default:
assignd_employee = it_inventory.get("LAP001", {})
print(assignd_employee.get("assigned_to", "No one"))