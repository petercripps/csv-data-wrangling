
from ast import Constant
from cgitb import text
from itertools import count
from logging import root
import tkinter as tk
from tkinter import EXTENDED, ttk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import os
from time import strftime
from turtle import width
from numpy import blackman 
import yaml
from csvwrangle import run_csv_wrangle
from readargs import read_yaml_file
import os

window = tk.Tk()
frame = tk.Frame()
frame.pack()
greeting = tk.Label(text="Vodbull .CSV Cleaner")
window.geometry("600x300")


def wrangle_callback():
    configdict = read_yaml_file("config.yaml")
    configdict["path"] = filepath
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
        

def file_select():
    file = filedialog.askopenfile(mode='r', filetypes=[('CSV Files', '*.csv')])
    global filepath
    if file:
        filepath = os.path.abspath(file.name)
        file_label = tk.Label(
            text=filepath,
            fg="black",
            bg="#F2F2F2",
            width=40,
            height=4,
).pack()
    
    

file_button = tk.Button(
    text="File Select",
    width=10,
    height=1,
    command=file_select,
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
file_button.pack()
help_button.pack()
quit_button.pack()
window.mainloop()