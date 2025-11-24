employees = [('Audrey', 'active'), ('Scarlet', 'inactive'), ('Monica', 'active')]
active_emails = {name: name.lower() + '@company.com' for name , status in employees if status == 'active'}
print(f"Active Emails: {active_emails}")

salary_usd = {'Audrey': 1000, 'Scarlet': 500, 'Monica': 670}
exchange_rate = 0.87
salary_eur = {}
for item, price in salary_usd.items():
    salary_eur[item] = price * exchange_rate 
print("USD:")
for name, price in salary_usd.items():
    print(f"{name}: {price}$")

print("\nEUR:")
for name, price in salary_eur.items():
    print(f"{name}: {price:.2f}€")



# .items() returns both the key and the value from a dictionary
# Example: ("Audrey", 1000)
# It lets us loop using: for name, salary in dictionary.items()

# :.2f formats a number to 2 decimal places
# :   → start formatting
# .2  → show exactly 2 digits after the decimal
# f   → format as a float (decimal number)
# Example: 123.456 becomes 123.46
