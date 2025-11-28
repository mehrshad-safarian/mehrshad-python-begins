# Basic student record: (student_id, name, major, enrollment_year, gpa)
student_record = (4003, "Rayan Scott", "computer science", 2021, 3.8)
transfer_record = (4004, "Liam Johnson", "mathematics", 2022, 3.6)

# semester courses : nested tuples with (course_id, name, credits, max_capacity)
course_listing = (
    ("CS101", "Introduction to programming", 3, 25),
    ("DS201", "Data Science fundamentals", 4, 20),
    ("MBA102", "Business management basics", 3, 60),
    ("MA203", "College Algebra", 3, 50)
)

# Accessing tuple elements
student_id = student_record[0]
student_name = student_record[1]

# Using tuple unpacking for cleaner code 
id_num, name, major, year, gpa = student_record
print(f"Students: {name}, Major: {major}")

# Count and index methodes 
programming_students = course_listing.count(("CS101", "Introduction to programming", 3, 25))
data_course_position = course_listing.index(("DS201", "Data Science fundamentals", 4, 20))

# mixing with lists dictionaries
enrollment_changes = [
    ("ADD", ("CS101", "Alex Jansen", "winter 2025")),
    ("DROP", ("MBA102", "Samantha Lee", "winter 2025"))
] #this is a nested tuple inside a list

department_courses = {
    "Computer Science": ("CS101", "CS205", "CS301"),
    "Mathematics": ("MA101", "MA202", "MA303"),
    "Business": ("MBA101", "MBA202", "MBA303"),
    "Data Science": ("DS201", "DS505", "DS707")
}

# Grade record: (student_id, course_id, semester, grade)
grade_records = (
    (4003, "CS101", "A", "Fall 2022"),
    (4004, "MA203", "A+", "Spring 2023"),
    (4003, "DS201", "B+", "Fall 2022")
)

# Current amd maximum enrollment comparison
current_enrollment = (22, 20, 43, 49)
max_capacities = (25, 20, 60, 50)
# 
for i in range(len(current_enrollment)):
    if current_enrollment[i] < max_capacities[i]:
        print(f"Seats available in {course_listing[i][1]}")
    else:
        print(f"{course_listing[i][1]} is full")

# Using zip to simplify the enrollment check
"""for course, current, maximum in zip(course_listing, current_enrollment, max_capacities):
    course_name = course[1]

    if current < maximum:
        print(f"Seats available in {course_name}")
    else:
        print(f"{course_name} is full")
"""
"""
✅ ZIP Summary (Easy Explanation)
zip() combines multiple lists/tuples by matching their elements by index.
Example:
a = (1, 2, 3)
b = ("A", "B", "C")
for x, y in zip(a, b):
    print(x, y)

Output:
1 A
2 B
3 C

zip(a, b) creates pairs:
(1, "A"), (2, "B"), (3, "C")
✅ Why we use it in your code
It lets you loop through:
course names
current enrollment
max capacity
all at the same time, cleanly:
for course, current, maximum in zip(course_listing, current_enrollment, max_capacities):
    if current < maximum:
        print(f"Seats available in {course[1]}")
    else:
        print(f"{course[1]} is full")
📌 One-sentence definition
zip() groups items from multiple sequences into matching pairs/triples so you can loop through them together."""

# Creating wait list entries 
waitlist_entry = (student_id, course_listing, "2025-01-10") 

try:
    student_id[1] = "Update Name"
except TypeError as e:
    print("Student record cannot be modified after creation")

# course enrollment tracking
course_enrollment = (
    
)