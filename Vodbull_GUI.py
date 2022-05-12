import tkinter as tk
from tkinter import ttk
#from Vodbull_Buttons import showerror, showwarning, showinfo

window = tk.Tk()
frame = tk.Frame()
frame.pack()
greeting = tk.Label(text="Vodbull .CSV Cleaner")

def wrangle_callback():
    print("Wrangle pressed")

wrangle_button = tk.Button(
    text="Wrangle",
    command=wrangle_callback,
    width=10,
    height=1,
    bg="grey",
    fg="black"
)

def sort_callback():
    print("Sort pressed")

sort_button = tk.Button(
    text="Sort",
    command=sort_callback,
    width=10,
    height=1,
    bg="grey",
    fg="black"
)

def help_callback():
    print("Help pressed")

help_button = tk.Button(
    text="Help",
    command=help_callback,
    width=10,
    height=1,
    bg="grey",
    fg="black"
)

quit_button = tk.Button(
    text="Quit",
    command=window.destroy,
    width=10,
    height=1,
    bg="grey",
    fg="black"
)

greeting.pack()
wrangle_button.pack()
sort_button.pack()
help_button.pack()
quit_button.pack()

window.mainloop()