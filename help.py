########################################################################
# help.py
# Print help from the help.txt file
#######################################################################
def print_help():
    helpfile = "help.txt"
    try:
        hfile = open(helpfile)
        content = hfile.read()
        hfile.close()
        print(content)
    except:
        print(f"ERROR Invalid or missing help file {helpfile}")

##########################
# Test program starts here
##########################

if __name__ == "__main__":
    # execute only if run as a script
    print("Testing...")
    
    if False:
        print_help()