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
    tk.Label(window, text="Directory").grid(row=1, column=0, sticky=tk.W)
    tk.Label(window, text="Input file").grid(row=2, column=0, sticky=tk.W)
    tk.Label(window, text="Output file").grid(row=3, column=0, sticky=tk.W)
    tk.Label(window, text="Error file").grid(row=4, column=0, sticky=tk.W)
    tk.Label(window, text="Sort by").grid(row=5, column=0, sticky=tk.W)
    
    # Create the entry objects and pack them using grid
    e0 = tk.Entry(window, textvariable=fpath)
    e0.grid(row=1, column=1, columnspan=2, sticky=tk.W)
    e0.insert(tk.END, config.configdict["path"])
    e1 = tk.Entry(window, textvariable=ifile)
    e1.grid(row=2, column=1, columnspan=2, sticky=tk.W)
    e1.insert(tk.END, config.configdict["csv-data"])
    e2 = tk.Entry(window, textvariable=vfile)
    e2.grid(row=3, column=1, columnspan=2, sticky=tk.W)
    e2.insert(tk.END, config.configdict["csv-vdata"])
    e3 = tk.Entry(window, textvariable=efile)
    e3.grid(row=4, column=1, columnspan=2, sticky=tk.W)
    e3.insert(tk.END, config.configdict["csv-edata"])
    e4 = tk.Entry(window, textvariable=scol)
    e4.grid(row=5, column=1, columnspan=2, sticky=tk.W)
    e4.insert(tk.END, config.configdict["sort"])

# Add buttons to window
def add_buttons(window):
    tk.Button(window, text='Directory', command=directory, padx=2,pady=2).grid(row=1,column=3, sticky=tk.W)
    tk.Button(window, text='Analyse', command=analyse, width=8, padx=2,pady=2).grid(row=11,column=0, sticky=tk.W)
    tk.Button(window, text='List', command=list, width=8, padx=2,pady=2).grid(row=11,column=1, sticky=tk.W)
    tk.Button(window, text="Save", command=save, width=8, padx=2,pady=2).grid(row=11,column=2, sticky=tk.W)
    tk.Button(window, text="Quit", command=window.destroy, width=8, padx=2,pady=2).grid(row=11,column=3, sticky=tk.W)

# Add checkbox to window
def add_checkbox(window, rownm, colnm, var, txt,cb_status):
    cb = tk.Checkbutton(window, text = txt, variable=var)
    if cb_status:
        cb.select()
    else:
        cb.deselect()
    cb.grid(column=rownm, row=colnm, sticky=tk.W)

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
    config.configdict["verbose"] = bool(check_verbose.get())
    config.configdict["rules"]["Uni"] = bool(check_unirule.get())
    config.configdict["rules"]["Email"] = bool(check_emailrule.get())
    config.configdict["rules"]["DOB"] = bool(check_dobrule.get())
    config.configdict["rules"]["UniYear"] = bool(check_uniyearrule.get())
    config.configdict["rules"]["Mobile"] = bool(check_mobilerule.get())
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
check_unirule = tk.IntVar()
check_emailrule = tk.IntVar()
check_dobrule = tk.IntVar()
check_uniyearrule = tk.IntVar()
check_mobilerule = tk.IntVar()

# 3. Add logo (keep this in the main programme, not as a function)
img = ImageTk.PhotoImage(Image.open("vodbulllogo.png"))
imglabel = tk.Label(win, image=img).grid(row=0, column=0, sticky=tk.W, columnspan=2) 

# 4. Create entry fields
add_entry_fields(win)

# 5. Add verbose checkbox
add_checkbox(win,0,6,check_verbose,"Verbose",config.configdict["verbose"])

# 6. Add rules checkboxes
tk.Label(win, text="Select rules:").grid(row=7, column=0, sticky=tk.W, columnspan=2)
add_checkbox(win,0,8,check_unirule,"Uni",config.configdict["rules"]["Uni"])
add_checkbox(win,1,8,check_emailrule,"Email",config.configdict["rules"]["Email"])
add_checkbox(win,2,8,check_dobrule,"DOB",config.configdict["rules"]["DOB"])
add_checkbox(win,0,9,check_mobilerule,"Mobile",config.configdict["rules"]["Mobile"])
add_checkbox(win,1,9,check_uniyearrule,"UniYear",config.configdict["rules"]["UniYear"])

# 7. Add buttons
add_blank_line(win, 10)
add_buttons(win)

# 7. Run it
win.mainloop()