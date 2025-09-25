# دریافت نام کشور
homeland = input("Pls enter the name of ur homeland :").strip()

# تعداد شهرهای مورد علاقه
num_countries = int(input("How many fav countries do u have?"))
# لیست برای ذخیره‌ی شهرها
countries = []

# گرفتن اسم شهرها و ذخیره کردن
for i in range(num_countries):
    country = input(f"Enter the name of country #{i+1}: ").strip()
    countries.append(country)

# بررسی حروف اول
vowels = ('a', 'e', 'i', 'o', 'u')
for country in countries: 
    if country.lower().startswith(vowels):
        print(f"{country.title()} starts with a vowel")
    else:
        print(f"{country.title()} starts with a consonant!")

# چاپ نتیجه‌ی نهایی
print(f"\nYour country: {country.title()}")
print("Your favorite countries:")
for c in countries:
    print(f"- {c.title()}")