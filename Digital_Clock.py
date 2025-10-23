import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a label to show the time
label = tk.Label(root, font=("Segoe UI", 60, "bold"), background="black", foreground="cyan")
label.pack(anchor="center")

# Function to update the time every second
def time():
    current_time = strftime("%H:%M:%S %p")
    label.config(text=current_time)
    label.after(1000, time)  # update every 1 second

time()
root.mainloop()