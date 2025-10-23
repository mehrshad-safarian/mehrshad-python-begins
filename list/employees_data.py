employees = [
    ["Arthur", "Right_hand", "100k"],
    ["Hosea", "Right_hand", "80k"],
    ["Rat", "sponger", "30k"] #by rat i meant that bastard named Micah bell :)
]
Right_hand_salaries = [emp[2] for emp in employees if emp[1] == "Right_hand"]
print(Right_hand_salaries)