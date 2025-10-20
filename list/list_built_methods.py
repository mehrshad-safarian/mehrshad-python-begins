laptop_inventory = ["hp-2021-001", "dell-2022-002", "lenovo2023"]
print(laptop_inventory)
tablet_inventory = ["ipad--2025-001", "surface-2024-002"]
print(tablet_inventory)
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
print(f"acquired_inventory: {acquired_inventory}")

laptop_inventory.sort()
laptop_inventory.reverse()
print(laptop_inventory)

laptop_inventory.insert(2,"asus-rog-2020")
print(laptop_inventory)

server_position = laptop_inventory.index("lenovo2023")
print(f"server_position: {server_position}")
dell_count = laptop_inventory.count("dell-2022-002")
print(f"dell count: {dell_count}")


complete_inventory = laptop_inventory + tablet_inventory
print(f"complete_inventory: {complete_inventory}")

branch_setups = tablet_inventory * 3
print(f"branch_setups: {branch_setups}")

total_tablet_inventory = len(tablet_inventory + branch_setups)
print(f"total tablets: {total_tablet_inventory}")

