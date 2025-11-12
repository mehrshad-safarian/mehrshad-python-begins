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

# Getting all asset ids in the inventory
asset_ids = it_inventory.keys()
print("Available Asset IDs: ", asset_ids)
for asset_id in it_inventory.keys():
    if asset_id.startswith("LAP"):
        print(f"Found laptop: {asset_id}")
    elif asset_id.startswith("MON"):
        print(f"Found monitor: {asset_id}")

laptop_count = 0
monitor_count = 0

for asset_id in it_inventory.keys():
    if asset_id.startswith("LAP"):
        laptop_count += 1
    elif asset_id.startswith("MON"):
        monitor_count += 1  
print(f"Total laptop's: {laptop_count}, Total monitor's: {monitor_count}")

if "LAP001" in it_inventory.keys():
    print("Laptop LAP001 is in inventory")

# Getting all equipment details 
all_equipment = it_inventory.values()

print("current status Report:")
for equipment in it_inventory.values():
    print(f"Type: {equipment['type']}")
    print(f"Model: {equipment['model']}")
    print(f"Status: {equipment['status']}")
    print(f"Location: {equipment['location']}")
    print("-" * 30)

print("\nMaintenance Overview:")
for equipment in it_inventory.values():
    print(f"{equipment['type']}: {equipment['maintenance']['condition']}")

print("\nEquipment by location:")
# Extract locations into two variables
a = it_inventory["LAP001"]["location"]
b = it_inventory["MON002"]["location"]

# Show both options to the user
print(f"A: {a}")
print(f"B: {b}")

# Ask user to choose one
user_choice = input("Choose a location (A/B): ").strip().upper()

# Determine which location was selected
if user_choice == "A":
    chosen_location = a
elif user_choice == "B":
    chosen_location = b
else:
    print("Invalid choice!")
    chosen_location = None

# If a valid location was chosen, display related equipment
# این حلقه این طوری میشه که اگه مقدار وجود داشته باشه 
# True
# باشه که طبق انتخابایی که گذاشتیم خروجی میده 
# ولی اگه نه چیزی رو کاربر انتخاب نکرده باشه 
# False 
# باشه هیچ مقداری بیرون نمیاد 
if chosen_location:
     for equipment in it_inventory.values():
        if equipment["location"] == chosen_location:
            print(f"{equipment['type']} - {equipment['model']}")


# Updating existing equipment infirmation
# Making copy of our original dict

# demo_inventory = it_inventory.copy()
# print("Before Update :")
# print(f"Status {demo_inventory['LAP001']['status']}")
# print(f"Location: {demo_inventory['LAP001']['location']}")
# print(f"Maintenance {demo_inventory['LAP001']['maintenance']['last_check']}")
# print(f"Status {demo_inventory['LAP001']['status']}")
# print("-" * 25)


# Make a copy of the original inventory
demo_inventory = it_inventory.copy()
print("Before Update:")
# Create a list of messages you want to print
info_list = [
    f"Status: {demo_inventory['LAP001']['status']}",
    f"Location: {demo_inventory['LAP001']['location']}",
    f"Maintenance: {demo_inventory['LAP001']['maintenance']['last_check']}",
    f"Status: {demo_inventory['LAP001']['status']}"
]
# Loop through each message and print it with a separator line
for info in info_list:
    print(info)
    print("-" * 25)

# Update method 
demo_inventory['LAP001'].update({
    "status": "Under Maintenance",
    "location": "IT Department",
    "maintenance": {
        "last_check": "2025-4-17",
        "next_check": "2026-7-17",
        "condition": "Excellent!"
    }
})
print("\nAfter Update:")
print(f"Status: {demo_inventory}")
info_list = [
    f"Status: {demo_inventory['LAP001']['status']}",
    f"Location: {demo_inventory['LAP001']['location']}",
    f"Maintenance: {demo_inventory['LAP001']['maintenance']['last_check']}",
    f"Status: {demo_inventory['LAP001']['status']}"
]
# Loop through each message and print it with a separator line
for info in info_list:
    print(info)
    print("-" * 25)


# Using copy() and popitem() methods 
demo_inventory = it_inventory.copy()
print("Initial inventory size:", len(demo_inventory))

demo_inventory["KBD001"] = {
    "type": "Keyboard",
    "model": "logitech MX keys", 
    "location": "IT storage"
}
print("\nAfter adding new item:")
print("inventory size:", len(demo_inventory))

# متد popitem()
# آخرین آیتم اضافه‌شده به دیکشنری رو حذف می‌کنه و برمی‌گردونه.
last_item_id, last_item_details = demo_inventory.popitem()
print(f"\nLast added item removed:")
print(f"Asset ID: {last_item_id}")
print(f"Type: {last_item_details['type']}")
print(f"model: {last_item_details['model']}")

print("Remaining inventory size:", len(demo_inventory))

empty_dictionary = {}
try:
    empty_dictionary.popitem()
except KeyError:
    print("\nCannot popitem() from empty inventory")

# set default values for existing  and non-existing fields
demo_inventory = it_inventory.copy()
print("working with LAP001")

status = demo_inventory["LAP001"].setdefault("status", "unknown")
print(f"Existing status:{status}")

notes = demo_inventory["LAP001"].setdefault("notes", "No additional info")
print(f"New field 'notes': {notes}")

print("\nWorking with MON002:")
service_tag = demo_inventory["MON002"].setdefault("service_tag", "not registered")
warranty_status = demo_inventory["MON002"].setdefault("warranty_status", "not assigned")
print(f"service_tag: {service_tag}")
print(f"warranty_status: {warranty_status}")


print("\nUpdated MON002 record:")
for key, value in demo_inventory["MON002"].items():
    print(f"{key}, {value}")




server_metrics = [["CPU_usage", "RAM_usage", "Disk_space"],
               ["Network_in", "Network_out", "Active_connections"],
                ["Response_time", "Error_rate", "Queue_length"]]
resource_Metrics = server_metrics[0]
print(resource_Metrics)
network_in = server_metrics[1][0] #this is how we refer to spacial item we have in mind
print(network_in)


default_structure = {
    "type": "Not Specified",
    "model": "Not Specified",
    "status": "Pending",
    "location": "IT Storage",
    "maintenance": {
        "last_check": 'Non',
        "next_check": "To be Scheduled",
        "condition": "Not Checked",
    }
}

new_laptop_ids = ["LAP003","LAP004","LAP005"]
new_laptops = dict.fromkeys(new_laptop_ids,default_structure)

print("Newly created inventory entries:")
for laptop_id, details in new_laptops.items():
    print(f"\nAsset ID: {laptop_id}")
    print(f"Status: {details['status']}")
    print(f"Location: {details['location']}")
    print(f"Maintenance Status: {details['maintenance']['condition']}")
