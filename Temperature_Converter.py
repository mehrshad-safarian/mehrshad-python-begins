#Get input from user
temp = float(input("Enter temperature: "))
unit = input("Enter unit (C for Celsius, F for Fahrenheit): ").upper()

if unit == "C":
    converted = (temp * 9/5) + 32
    print(f"{temp}°C is {converted}°F")
elif unit == "F":
    converted = (temp - 32) * 5/9
    print(f"{temp}°F is {converted}°C")
else:
    print("Invalid unit!")
