import time
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

demo_inventory = it_inventory.copy()

print("initial inventory contents:")
for asset_id in demo_inventory:
    print(f"Asset: {asset_id}")

print(f"\nIntial inventory size: {len(demo_inventory)}")

print("\nClearing inventory...")
time.sleep(5)
demo_inventory.clear()

print(f"Inventory size after clear:{len(demo_inventory)}")
print(f"Inventory contents: {demo_inventory}")

demo_inventory["NEW001"] = {
    "type": "Laptop",
    "status": "New"
}
print(f"new will be : {demo_inventory}")