# Defineing the regions
western_states = ["California", "Oregon", "Washington", "Nevada", "Arizona",
                  "Colorado", "Utah", "Idaho", "Montana", "Wyoming"]

eastern_states = ["New York", "Florida", "Georgia", "Virginia", "Maine",
                  "Pennsylvania", "New Jersey", "Massachusetts", "Maryland"]

# Getting the input
state = input("U see we are here to find out about eastern and western geographical loc so Enter the U.S. state name u have in ur mind pls : ").strip().title()

# Classifying the catagory state belongs
if state in western_states:
    print(f"{state} is in the Western United States.")
elif state in eastern_states:
    print(f"{state} is in the Eastern United States.")
else:
    print(f"Sorry, I don't have {state} in my list.")