<<<<<<< HEAD
import tkinter as tk
from tkinter import ttk
from Vodbull_Buttons import *

root = tk.Tk()
root.title("Tkinter MessageBox")
root.resizable(False, False)
root.geometry("300x150")

options = {'fill': 'both', 'padx': 10, 'pady': 10, 'ipadx': 5}

ttk.Button(
    root,
    text='Show an error message',
    command=lambda: showerror(
        title='Error',
        message='This is an error message.')
).pack(**options)

ttk.Button(
    root,
    text='Show an information message',
    command=lambda: showinfo(
        title='Information',
        message='This is an information message.')
).pack(**options)

ttk.Button(
    root,
    text='Show a warning message',
    command=lambda: showwarning(
        title='Warning',
        message='This is a warning message.')
).pack(**options)




window = tk.Tk()
root.mainloop()
=======
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

root = tk.Tk()
root.title("Tkinter MessageBox")
root.resizable(False, False)
root.geometry("300x150")

options = {'fill': 'both', 'padx': 10, 'pady': 10, 'ipadx': 5}

ttk.Button(
    root,
    text='Show an error message',
    command=lambda: showerror(
        title='Error',
        message='This is an error message.')
).pack(**options)

ttk.Button(
    root,
    text='Show an information message',
    command=lambda: showinfo(
        title='Information',
        message='This is an information message.')
).pack(**options)

ttk.Button(
    root,
    text='Show a warning message',
    command=lambda: showwarning(
        title='Warning',
        message='This is a warning message.')
).pack(**options)




window = tk.Tk()
root.mainloop()
>>>>>>> b07905f18d7249b663d91d3c07194efc691a9ec6
