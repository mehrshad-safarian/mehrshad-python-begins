laptop_inventory = ["hp-2021-001", "dell-2022-002", "lenovo2023"]
print(laptop_inventory)
laptop_inventory.append(input("pls enter ur considered laptop :"))
print(laptop_inventory)


primery_inventory = ["hp-2021-001", "dell-2022-002", "lenovo2023"]
print(f"primery inventory: ,{primery_inventory}")
acquired_inventory = ["hp-2025-700", "dell-2024-583"]
primery_inventory.extend(acquired_inventory)
print(f"primery_inventory after acquired inventory: ,{primery_inventory}")
primery_inventory.insert(1,"vaio-2025-726")
primery_inventory.remove("hp-2021-001")
print(f"final list of prymeries : {primery_inventory}")
transferred_device = primery_inventory.pop()
print(f"transferred device  : {transferred_device} ")

acquired_inventory.clear()
print(acquired_inventory)

laptop_inventory.sort()
laptop_inventory.reverse()
print(laptop_inventory)