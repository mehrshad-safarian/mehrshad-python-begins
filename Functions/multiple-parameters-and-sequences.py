# Multiple parameters
def make_schedule(period1, period2):
    schedule = ("[1st] " +  period1.title() + ", [2nd] " + period2.title())
    return schedule

student_schedule = make_schedule("math", "Digital System Foundation")
print("Schedule:", student_schedule)

def format_info(name, age, school):
    return "Student:" + name + "\nAge:" + str(age) + "\nSchool:" + school
print(format_info("Sydney Sweeney", 28, "Saint George's School"))
print()

# Sequence
first_name = "sydney"
def hat_available(color):
    hat_colors = "brown, black, purple, white, green, grey, pink"
    return(color.lower() in hat_colors)
hats_in_stock =  hat_available("brown")
print("Available hats are:", hats_in_stock)


first_name = "sydney"

def hat_available(*colors):  # Taking unlimited number of arguments
    hat_colors = "brown, black, purple, white, green, grey, pink"
    results = []
    for color in colors:
        results.append(color.lower() in hat_colors)
    return results 
hats_in_stock = hat_available("brown", "pink", "white")
print("Available hats are:", hats_in_stock)





def hat_available(*colors):
    hat_colors = ["brown", "black", "purple", "white", "green", "grey", "pink"]
    available = [c for c in colors if c.lower() in hat_colors]
    return available

hats_in_stock = hat_available("brown", "pink", "white", "red")
print("Available hats are:", hats_in_stock)

