courses = []  # list to store course info

while True:
    name = input("Enter the course name (type 'exit' to stop): ")
    if name.lower() == "exit":
        print("Calculating GPA...")
        break

    # Get grade
    try:
        grade = float(input(f"Enter the grade for {name}: "))
    except ValueError:
        print("Invalid grade. Try again.")
        continue

    # Get units
    try:
        unit = float(input(f"Enter the units for {name}: "))
    except ValueError:
        print("Invalid unit. Try again.")
        continue

    # Store as a dictionary
    courses.append({"name": name, "grade": grade, "unit": unit})
    print(f"Added course: {name}, grade: {grade}, units: {unit}")

# Calculate weighted GPA
if courses:
    total = sum(course["grade"] * course["unit"] for course in courses)
    total_units = sum(course["unit"] for course in courses)
    gpa = total / total_units
    print("\nCourses entered:")
    for course in courses:
        print(f"{course['name']}: grade {course['grade']}, units {course['unit']}")
    print(f"\nYour weighted GPA is: {gpa}")
else:
    print("No courses entered.")
