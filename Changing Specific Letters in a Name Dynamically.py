name = "mehrshad"
new_name = ""

for ltr in name:
    # If the letter is 'y', make it uppercase
    if ltr.lower() == "s":
        new_name += ltr.upper()
    else:
        new_name += ltr

print(f"Original name: {name}")
print(f"Transformed name: {new_name}")
