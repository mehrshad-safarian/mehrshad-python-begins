'''
Task: Define a Car class
Create a class named Car.
Inside the class, define a method called details() that prints:
Make (e.g., "Toyota")
Model (e.g., "Corolla")
Year (e.g., 2020)
Create an object of the Car class.
Call the details() method to display the information.
'''
# Define the Car class
class Car:
    # Define the method to print car details
    def details(self):
        print("Make (e.g., 'Toyota')")
        print("Model (e.g., 'Corolla')")
        print("Year (e.g., 2020)")
# Create an object of Car
my_car = Car()
# Call the details method
my_car.details()
# تعریف کلاس Car با سازنده (__init__)
class Car:
    def __init__(self, make, model, year):
        # مقادیر ورودی رو به ویژگی‌های شیء اختصاص میدیم
        self.make = make
        self.model = model
        self.year = year

    def details(self):
        # چاپ مشخصات با f-string
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

# ایجاد شیء و فرستادن مشخصات موقع ساخت
my_car = Car("Lamborghini", "Gallardo", 2005)

# فراخوانی متد برای نمایش مشخصات
my_car.details()