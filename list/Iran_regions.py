#Define province group

western_provinces = [
    "Kermanshah", "Kurdistan", "Ilam", "Lorestan", "Hamadan",
    "West Azerbaijan", "East Azerbaijan", "Ardabil", "Zanjan"
]

eastern_provinces = [
    "Khorasan Razavi", "South Khorasan", "North Khorasan",
    "Sistan and Baluchestan", "Kerman"
]

northern_provinces = [
    "Gilan", "Mazandaran", "Golestan", "Qazvin", "Alborz", "Tehran"
]

southern_provinces = [
    "Hormozgan", "Bushehr", "Khuzestan", "Fars"
]

central_provinces = [
    "Markazi", "Qom", "Isfahan", "Yazd", "Semnan", "Chaharmahal and Bakhtiari"
]

#Start the program

print("👋 Welcome! I can tell you which region of Iran a province belongs to.")
print("Type 'exit' anytime to quit.\n")

while True:
    province = input("Enter a province name: ").strip().title()

    if province.lower() == "exit":
        print("👋 Goodbye! Have a great day!")
        break

    if province in western_provinces:
        print(f"✅ {province} is in Western Iran.")
    elif province in eastern_provinces:
        print(f"✅ {province} is in Eastern Iran.")
    elif province in northern_provinces:
        print(f"✅ {province} is in Northern Iran.")
    elif province in southern_provinces:
        print(f"✅ {province} is in Southern Iran.")
    elif province in central_provinces:
        print(f"✅ {province} is in Central Iran.")
    else:
        print(f"❓ Sorry, I don't have {province} in my list.")

    choice = input("\nWould you like to check another province? (yes/no): ").strip().lower()
    if choice not in ["yes", "y"]:
        print("👋 Goodbye! Stay safe and take care!")
        break

    print()
