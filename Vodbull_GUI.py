import tkinter as tk
from tkinter import ttk
#from Vodbull_Buttons import showerror, showwarning, showinfo

window = tk.Tk()
frame = tk.Frame()
frame.pack()
greeting = tk.Label(text="Vodbull .CSV Cleaner")

wrangle_button = tk.Button(
    text="Wrangle",
    width=10,
    height=1,
    bg="grey",
    fg="black"
)

sort_button = tk.Button(
    text="Sort",
    width=10,
    height=1,
    bg="grey",
    fg="black"
)

help_button = tk.Button(
    text="Help",
    width=10,
    height=1,
    bg="grey",
    fg="black"
)

greeting.pack()

wrangle_button.pack()
sort_button.pack()
help_button.pack()

window.mainloop()