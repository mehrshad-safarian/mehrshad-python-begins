my_dict = {
    'name': input("pls enter ur name: "),
    'age': input("pls enter ur age :"),
    'email': input("pls enter ur email address:")
}
print(my_dict)

# i used ai and turn this to how profetional code of it whould  be look like
# which >>> Name: can’t be empty, contain numbers, or only spaces. Age: must be numeric and not empty. Email: must look like a real email (contain @ and .).

# Create an empty dictionary
# my_dict = {}
# # --- NAME VALIDATION ---
# while True:
#     name = input("Please enter your name: ").strip()
#     if not name:  # Empty input
#         print("❌ Name cannot be empty.")
#     elif any(char.isdigit() for char in name):  # Contains numbers
#         print("❌ Name cannot contain numbers.")
#     elif name.isspace():  # Just spaces
#         print("❌ Name cannot be just spaces.")
#     else:
#         my_dict['name'] = name
#         break

# # --- AGE VALIDATION ---
# while True:
#     age = input("Please enter your age: ").strip()
#     if not age:
#         print("❌ Age cannot be empty.")
#     elif not age.isdigit():
#         print("❌ Age must contain only numbers.")
#     else:
#         my_dict['age'] = int(age)
#         break

# # --- EMAIL VALIDATION ---
# while True:
#     email = input("Please enter your email address: ").strip()
#     if not email:
#         print("❌ Email cannot be empty.")
#     elif "@" not in email or "." not in email.split("@")[-1]:
#         print("❌ Invalid email format. Example: user@example.com")
#     else:
#         my_dict['email'] = email
#         break

# # --- FINAL OUTPUT ---
# print("\n✅ Your data:")
# print(my_dict)
