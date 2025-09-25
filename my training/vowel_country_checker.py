# getting the name of counties
homeland = input("Pls enter the name of ur homeland :").strip()

# number of fav countries
num_countries = int(input("How many fav countries do u have?"))
# list for saving the countries
countries = []

# getting the name of the countries and storing them
for i in range(num_countries):
    country = input(f"Enter the name of country #{i+1}: ").strip()
    countries.append(country)

# checking the first letters for being vowels
vowels = ('a', 'e', 'i', 'o', 'u')
for country in countries: 
    if country.lower().startswith(vowels):
        print(f"{country.title()} starts with a vowel")
    else:
        print(f"{country.title()} starts with a consonant!")

# printing the final output
print(f"\nYour homeland: {homeland.title()}")
print("Your favorite countries:")
for c in countries:
    print(f"- {c.title()}")