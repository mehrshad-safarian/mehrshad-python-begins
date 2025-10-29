department_assignment = {'emp_101': 'sales', 'emp_102': 'finance', 'emp_103': 'IT'}

# key_list = list(department_assignment.keys())
# key_list.sort()
# for employee_id in key_list:
#     print(employee_id, '-->', department_assignment[employee_id])

for  employee_id in sorted(department_assignment):
    print(employee_id, '-->', department_assignment[employee_id])


for letter in 'Iran':
    print(letter.upper())

time_remaining = 3
while time_remaining > 0:
    print('System shutdown in:' * time_remaining)
    time_remaining  -=1
