
from itertools import count
import tkinter as tk
from tkinter import EXTENDED, ttk
from tkinter import *
from time import strftime 
import yaml
from csvwrangle import run_csv_wrangle
from readargs import read_yaml_file

window = tk.Tk()
frame = tk.Frame()
frame.pack()
greeting = tk.Label(text="Vodbull .CSV Cleaner")

def wrangle_callback():
    configdict = read_yaml_file("config.yaml")
    run_csv_wrangle(configdict)

wrangle_button = tk.Button(
    text="Wrangle",
    command=wrangle_callback,
    width=10,
    height=1,
    bg="grey",
    fg="black"
)



def sort_box(window):
    lb = Listbox(window, selectmode=EXTENDED, width=10)
    lb.grid(column=3, row=0, rowspan=4)
    count = 0
    for entry in col_names :
        sb.insert(count, entry)
        count +=1
    return lb


sort_button = tk.Button(
    text="Sort",
    command=sort_box,
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