# Example 2: Naming Conventions
"""class userAccount:
    def **init**(self,UserName,Email,Age):
        self.UserName=UserName
        self.Email=Email
        self.Age=Age
    
    def display_INFO(self):
        print(f"User: {self.UserName}, Email: {self.Email}, Age: {self.Age}")
"""
# Violations:
# Incorrect class name (should be CamelCase)
# Incorrect method name (should be snake_case)
# Inconsistent naming conventions
# Missing spaces after commas

class UserAccount:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age
    
    def display_info(self):
        print(f"User: {self.username}, Email: {self.email}, Age: {self.age}")

# Create an object
print("Please enter ur information down below")

username = input("Please enter ur name: ")
email = input("Please enter ur email: ")
age = int(input("Please enter ur age: "))

user1 = UserAccount(username, email, age)
# Call the method
user1.display_info()
