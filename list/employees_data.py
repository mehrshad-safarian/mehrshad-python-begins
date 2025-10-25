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
print(f"Average Right salary dutch payes : ${average_Right_hand_salaries}")

# Knowing the positions and using set to remove repitations
positions = set([emp[1] for emp in employees])
print(positions)
print()

employees_data = [
    [1000, 63000, 'IT', 'Active'],
    [2000, 75000, 'Sales', 'Active'],
    [3000, 45000, 'HR', 'InActive'],
    [1001, 54000, 'IT', 'Active']
]

adjusted_salaries = [employee[1] + 5000 for employee in employees_data]
print(f"adjusted salaries : {adjusted_salaries}")
IT_department = [employee[1] for employee in employees_data if employee[2] == 'IT']
print(f"IT department salaries : {IT_department}")
active_employee_ids = [employee[0] for employee in employees_data if employee[3] =='Active']
print(f"active employees ids : {active_employee_ids}")
department_codes = [employee[2] for employee in employees_data]
formatted_codes = [code.lower() for code in department_codes]
print(f"department codes : {formatted_codes}")
high_salary_employees = [
    [employee for employee in employees_data if employee[1] > 55000],
    [emp for emp in Right_hand_salaries if emp > 55000]
    
]
print(f"high salary employees : {high_salary_employees}")