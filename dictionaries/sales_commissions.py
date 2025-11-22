commissions = [sale * 0.05 for sale in sales_transactions] # type: ignore

commissions = []
for sale in sales_transations :
    commissions.append(sale * 0.05)
print(commissions)

employee_names = ['Megan Fox', 'Sydney Sweeny' ,'Sophie Turner' ]
email_dict = {name: name.lower().replace(' ') + '@company.com' for name in employee_names}
print(email_dict)