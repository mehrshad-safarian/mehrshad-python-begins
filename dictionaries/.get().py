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
assigned_employee = it_inventory.get("LAP001", {})
print(assigned_employee.get("assigned_to", "No one"))
# .get("LAP001", {}) → returns the LAP001 dictionary if it exists, otherwise an empty {}.
# .get("assigned_to", "No one") → looks for the employee name inside it.

department = it_inventory.get("LAP001", {}).get("department", {})
print(f"department: ", {department})
# Both examples use two .get() calls, but in different ways.
# In the first one, the second .get() is used inside print() after storing the first result in a variable.
# In the second one, both .get() calls are chained together in a single line (nested call).
# So the logic is the same — only the structure differs:
# first → two steps (clearer)
# second → nested .get() (shorter)

# going deeper (nested .get()):
purchase_info = it_inventory.get("LAP001", {}).get("purchase_info", {})
print(purchase_info.get("date", "unknown"))
print(f"{purchase_info.get("cost", "unknown")} $")
print(purchase_info.get("supplier", "unknown"))
# The first .get("LAP001", {}) finds the laptop dictionary.
# The second .get("purchase_info", {}) goes inside that dictionary.
# Finally, each .get() reads one key safely (date, cost, supplier).

# basic iteration through inventory items 
for asset_id, asset_info in it_inventory.items():
    print(f"Asset ID: {asset_id}")
    print(f"Equipment Type: {asset_info['type']}")
    print(f"Current Status: {asset_info['status']}")
    print("-" * 25)

print("Current Equipment Status Report: ")
for asset_id, asset_info in it_inventory.items():
    location = asset_info['location']
    status = asset_info['status']
    model = asset_info['model']
    print(f"{asset_id}: {model} - located in {location} - status: {status}")

print("\nMaintenance Summary:")
for asset_id, asset_info in it_inventory.items():
    last_check = asset_info['maintenance']['last_check']
    condition = asset_info["maintenance"]['condition']
    print(f"{asset_id} - Last check: {last_check}, Condition: {condition}")