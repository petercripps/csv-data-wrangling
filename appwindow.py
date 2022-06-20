########################################################################
# appwindow.py
# Creates a dialog window for changing parameters and submitting CSV.
# See http://effbot.org/tkinterbook/ for how this works.
########################################################################
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import yaml
import config
from csvanalyser import run_csv_analyse, csv_list

yfile = "config.yaml"

# Add entry fields to window
def add_entry_fields(window):
    # Create the label objects and pack them using grid
    tk.Label(window, text="Directory", justify=tk.LEFT).grid(row=1, column=0)
    tk.Label(window, text="Input file", justify=tk.LEFT).grid(row=2, column=0)
    tk.Label(window, text="Output file", justify=tk.LEFT).grid(row=3, column=0)
    tk.Label(window, text="Error file", justify=tk.LEFT).grid(row=4, column=0)
    tk.Label(window, text="Sort by", justify=tk.LEFT).grid(row=5, column=0)
    
    # Create the entry objects and pack them using grid
    e0 = tk.Entry(window, textvariable=fpath)
    e0.grid(row=1, column=1)
    e0.insert(tk.END, config.configdict["path"])
    e1 = tk.Entry(window, textvariable=ifile)
    e1.grid(row=2, column=1)
    e1.insert(tk.END, config.configdict["csv-data"])
    e2 = tk.Entry(window, textvariable=vfile)
    e2.grid(row=3, column=1)
    e2.insert(tk.END, config.configdict["csv-vdata"])
    e3 = tk.Entry(window, textvariable=efile)
    e3.grid(row=4, column=1)
    e3.insert(tk.END, config.configdict["csv-edata"])
    e4 = tk.Entry(window, textvariable=scol)
    e4.grid(row=5, column=1)
    e4.insert(tk.END, config.configdict["sort"])

# Add buttons to window
def add_buttons(window):
    tk.Button(window, text='Directory', command=directory, padx=2,pady=2).grid(row=1,column=2)
    tk.Button(window, text='Analyse', command=analyse, width=8, padx=2,pady=2).grid(row=8,column=0)
    tk.Button(window, text='List', command=list, width=8, padx=2,pady=2).grid(row=8,column=1)
    tk.Button(window, text="Save", command=save, width=8, padx=2,pady=2).grid(row=8,column=2)
    tk.Button(window, text="Quit", command=window.destroy, width=8, padx=2,pady=2).grid(row=8,column=3,)

# Add a checkbox to window
def add_checkbox(window):
    cb = tk.Checkbutton(window, text = "Verbose", variable=check_verbose, justify=tk.LEFT)
    if config.configdict["verbose"]:
        cb.select()
    else:
        cb.deselect()
    cb.grid(column=0, row=6)

# Add a blank line (i.e. a lable with no text)
def add_blank_line(window, line):
    tk.Label(window, text='', justify=tk.LEFT).grid(column=0, row=line)

# Called when the 'Analyse' button selected
def analyse():
    # Save all changes to YAML file
    save()
    # Run the CSV analyser    
    run_csv_analyse()

# Called when the 'List' button selected
def list():
    # Save all changes to YAML file
    save()
    # Run the CSV lister    
    csv_list()

# Called when the 'Directory' button selected
def directory():
    # get a directory path by user
    savedfilepath = config.configdict["path"]
    filepath=filedialog.askdirectory(initialdir=savedfilepath,
                                    title="Dialog Box")
    config.configdict["path"] = filepath

# Called when the 'Save' button is selected also the 'Analyse'
# and 'List' buttons.
# Dump updated config info to the YAML file
def save():
    print(f"Saving any config changes to {yfile}")
    # Make sure configdict (i.e. a global) is reinitialised prior to saving as, if an analyse has already been
    # performed column names will have been modified by adding an 'Error' column.
    config.configdict = config.init_config()
    # Read contents of all fields
    config.configdict["path"] = fpath.get()
    config.configdict["csv-data"] = ifile.get()
    config.configdict["csv-vdata"] = vfile.get()
    config.configdict["csv-edata"] = efile.get()
    config.configdict["sort"] = scol.get()
    if check_verbose.get() == 1:
        config.configdict["verbose"] = True
    else:
        config.configdict["verbose"] = False
    # Save to YAML file
    with open(yfile, 'w') as file:
        data = yaml.dump(config.configdict, file)

# Program starts here.
# 1. Build the window
win = tk.Tk()
win.wm_title("CSV Analyser")

# 2. Define variables for collecting inputs
fpath = tk.StringVar()
ifile = tk.StringVar()
vfile = tk.StringVar()
efile = tk.StringVar()
scol = tk.StringVar()
check_verbose = tk.IntVar()

# 3. Add logo (keep this in the main programme, not as a function)
img = ImageTk.PhotoImage(Image.open("vodbulllogo.png"))
imglabel = tk.Label(win, image=img).grid(row=0, column=0) 

# 4. Create entry fields
add_entry_fields(win)

# 5. Add checkbox
add_checkbox(win)

# 6. Add buttons
add_blank_line(win, 7)
add_buttons(win)

# 7. Run it
win.mainloop()