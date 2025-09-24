'''
Task: Define a Student class with dynamic info
Create a class named Student.
Add a constructor (__init__) that takes name, age, and grade as parameters and stores them in the object.
Define a method display_info() that prints the students name, age, and grade.
Create two different Student objects with different info.
Call display_info() for each object.
'''
# Define the Student class
class Student:
    # Constructor to store student info
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    # Method to display info
    def display_info(self):
        print("name:", self.name)
        print("age:", self.age)
        print("grade:", self.grade)

# Create two Student objects
 # Get info from the user for the first student
name0 = input("Enter the name of the first student: ")
age0 = input("Enter the age of the first student: ")
grade0 = input("Enter the grade of the first student: ")
student0 = Student(name0, age0, grade0)

 # Get info from the user for the second student
name1 = input("Enter the name of the second student: ")
age1 = input("Enter the age of the second student: ")
grade1 = input("Enter the grade of the second student: ")
student1 = Student(name1, age1, grade1)

# Display their info
student0.display_info()
student1.display_info()
git restore "Coding Exercise sec1/Coding Exercise 1 Printing with Python Your First Step into Coding.py"