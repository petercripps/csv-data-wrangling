
from ast import Constant
from cgitb import text
from itertools import count
from logging import root
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import os
from time import strftime
from turtle import width
from numpy import blackman 
import config
from csvanalyse import run_csv_analyse
import os
window = tk.Tk()
window.title(" Vodbull .CSV Cleaner ")
frame = tk.Frame()
frame.pack()
window.geometry("700x400")
border_effects = {
"sunken": tk.SUNKEN}

def analyse_callback():
    config.configdict["path"] = filepath
    run_csv_analyse()

analyse_button = tk.Button(
    text="Analyse",
    command=analyse_callback,
    width=30,
    height=3,
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
    width=30,
    height=3,
    bg="grey",
    fg="black"
)

def help_callback():
    print("Help pressed")

help_button = tk.Button(
    text="Help",
    command=help_callback,
    width=30,
    height=3,
    bg="grey",
    fg="black"
)
        

def file_select():
    file = filedialog.askopenfile(mode='r', filetypes=[('CSV Files', '*.csv')])
    global filepath
    if file:
        filepath = os.path.abspath(file.name)
        file_label = tk.Label(
            text=(filepath),
            fg="black",
            bg="#F2F2F2",
            width=50,
            height=5,).place(x=200,y=5)
    
    

file_button = tk.Button(
    text="File Select",
    width=25,
    height=3,
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

analyse_button.place(x=15,y=330)
sort_button.place(x=240,y=330)
file_button.place(x=15,y=10)
help_button.place(x=465,y=330)
quit_button.place(x=600,y=10)
window.mainloop()