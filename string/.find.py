#find
fullname = "mehrshad_safarian_khaki"
print(f"find the index of the first underscore",{fullname.find("_")},"\n")
print(f"full name : ", {fullname},"first name is : ", fullname[:8])
name_first_ltr = fullname.find("mehrshad")
print()
print(name_first_ltr, '= starting index for "mehrshad"')
location = fullname.find("a")

while location >= 0:
    print("'a' at index =", location)
    location = fullname.find("a", location + 1)
    
print("search for'khaki'in the sub-string:", fullname[9:24])
khaki_here = fullname.find("khaki")
print('"khaki" found in fullname[9:24] sub-string search at index ', khaki_here)