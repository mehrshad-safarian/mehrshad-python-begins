# Basic student record: (student_id, name, major, enrollment_year, gpa)
student_record = (4003, "Rayan Scott", "computer science", 2021, 3.8)
transfer_record = (4004, "Liam Johnson", "mathematics", 2022, 3.6)

# semester courses : nested tuples with (course_id, name, credits, max_capacity)
course_listing = (
    ("CS101", "Introduction to programming", 3, 25),
    ("DS201", "Data Science fundamentals", 4, 20),
    ("MBA102", "Business management basics", 3, 60)
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