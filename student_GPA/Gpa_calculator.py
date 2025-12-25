import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

root = tk.Tk()
root.title("GPA Calculator")
root.geometry("500x400")

courses = []

# Labels and entries
tk.Label(root, text="Course Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Grade").pack()
grade_entry = tk.Entry(root)
grade_entry.pack()

tk.Label(root, text="Units").pack()
unit_entry = tk.Entry(root)
unit_entry.pack()

# Treeview (table) setup
columns = ("Course", "Grade", "Units")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack(pady=10)

# Add course function
def add_course():
    name = name_entry.get()
    try:
        grade = float(grade_entry.get())
        unit = float(unit_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Grade and Units must be numbers")
        return

    courses.append({"name": name, "grade": grade, "unit": unit})
    tree.insert("", tk.END, values=(name, grade, unit))

    # Clear entries
    name_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)
    unit_entry.delete(0, tk.END)

# Calculate GPA function
def calculate_gpa():
    if not courses:
        messagebox.showerror("Error", "No courses added")
        return

    total = sum(c["grade"] * c["unit"] for c in courses)
    total_units = sum(c["unit"] for c in courses)
    gpa = total / total_units

    messagebox.showinfo("GPA Result", f"Your weighted GPA is: {gpa:.2f}")

# Buttons
tk.Button(root, text="Add Course", command=add_course).pack(pady=5)
tk.Button(root, text="Calculate GPA", command=calculate_gpa).pack(pady=5)

root.mainloop()
