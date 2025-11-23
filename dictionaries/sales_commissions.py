# Sales data
sales_transactions = [1000, 1500, 800, 2200]

# Using a for loop to calculate commissions
commissions = []  # empty list to store commission values

for sale in sales_transactions:
    commission_amount = sale * 0.05      # calculate 5% commission
    commissions.append(commission_amount)

# Show result
print("Sales:", sales_transactions)
print("Commissions (5%):", commissions)

employee_names = ['Megan Fox', 'Sydney Sweeny' ,'Sophie Turner' ]
email_dict = {
    name: name.lower().replace(' ', '.') + '@company.com' 
    for name in employee_names
    }
print(email_dict)

email_dict =  {}
for name in employee_names:
    email_dict[name] = name.lower().replace(' ', '.') + '@company.com'
    print(email_dict)