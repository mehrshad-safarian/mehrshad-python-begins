cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "tehran", "shiraz"]
search_letter = "a"
total = 0

for city_name in cities:
    total += city_name.lower().count(search_letter)

print(f"The total # of \"{search_letter}\" found in the list is:", {total})

cities = []

cities = []

while True:
    num = int(input("How many cities do you want to enter? (must be more than 3): "))
    if num < 3:
        print("❌ You must enter at least 3 cities. Try again.")
    else:
        break

for i in range(num):
    city = input(f"Please enter the name of city {i+1}: ").strip()
    cities.append(city)

search_letter = "a"
total = 0

for city_name in cities:
    total += city_name.lower().count(search_letter)

print(f'The total # of "{search_letter}" found in your list is: {total}')
