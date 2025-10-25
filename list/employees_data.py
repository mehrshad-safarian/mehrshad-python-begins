employees = [
    ["Arthur", "Right_hand", "100k"],
    ["Hosea", "Right_hand", "80k"],
    ["Rat", "sponger", "30k"] #by rat i meant that bastard named Micah bell :)
]
# remove the "k" and convert to integer
Right_hand_salaries = [int(emp[2].replace("k", "")) * 1000 for emp in employees if emp[1] == "Right_hand"]
print(employees)
print(f"Right handes fee : ${Right_hand_salaries[0]}, ${Right_hand_salaries[1]}")
average_Right_hand_salaries = sum(Right_hand_salaries) / len(Right_hand_salaries)
print(f" Average Right salary dutch payes : ${average_Right_hand_salaries}")