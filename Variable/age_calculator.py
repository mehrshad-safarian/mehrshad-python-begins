from datetime import datetime
#current_year = 2025
current_year = datetime.now().year
birth_year = input("Pls enter the year u were born at :")
age = current_year - int(birth_year)
print(f"niiice".title(),"my friend! so u are", age ,"year old!")
