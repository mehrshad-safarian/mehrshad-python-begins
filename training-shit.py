import tkinter as tk
from time import strftime


# main window
root = tk.Tk()
root.title("Digital Clock")
root.attributes("-fullscreen", True)
root.configure(bg="black")


# screen info (for responsive sizing)
screen_height = root.winfo_screenheight()

time_font_size = int(screen_height * 0.2)
date_font_size = int(screen_height * 0.06)


# widgets
time_label = tk.Label(
    root,
    font=("Segoe UI", time_font_size, "bold"),
    bg="black",
    fg="cyan"
)
time_label.pack(expand=True)

date_label = tk.Label(
    root,
    font=("Segoe UI", date_font_size),
    bg="black",
    fg="white"
)
date_label.pack(pady=10)


def update_clock():
    time_label.config(text=strftime("%H:%M:%S"))
    date_label.config(text=strftime("%A  |  %d %B %Y"))
    root.after(1000, update_clock)


update_clock()


# simple exit
root.bind("<Escape>", lambda e: root.destroy())
root.bind("<Button-1>", lambda e: root.destroy())

root.mainloop()
