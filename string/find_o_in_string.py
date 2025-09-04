# find_o_in_string.py

work_tip = "good code has meaningful variable names"
location = work_tip.find("o")

while location >= 0:
    print("'o' at index =", location)
    location = work_tip.find("o", location + 1)