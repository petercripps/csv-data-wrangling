########################################################################
# readargs.py
# Read the arguments from the command line. Arguments not provided will
# be taken from the config file config.yaml.
# Note that this uses Python's new 'match' statement which has only been
# available from v3.10. Ensure you have that version or later installed.
########################################################################

import sys
import config
from help import print_help

# The list of valid operations that can be specified on the command line.
valid_ops = ["analyse", "list"]

# Reads a list of arguments or, if none, a file in yaml format.
# Parameters:
#   args : List - The command line arguments 
# Returns:
#   None 
def read_args(args):
    if len(args) == 1:
        print("No arguments provided so using YAML file")
        return
    # If first argument is -h print help and return.
    if args[1] == '-h':
        print_help()
        return
    
    # Check if first argument is a valid operation and save then
    #  set index to begin at second argument
    if args[1] in valid_ops:
        config.configdict["operation"] = args[1]
        i = 2
    else:
        # Start looking at parameters from first argument
        i = 1
    # Read remaining arguments starting at second argument
    try:
        while i < len(args):
            match args[i]:     
                case '-i':
                    config.configdict["csv-data"] = args[i + 1]
                    i += 1
                case '-o':
                    config.configdict["csv-vdata"] = args[i + 1]
                    i += 1
                case '-e':
                    config.configdict["csv-edata"] = args[i + 1]
                    i += 1
                case '-p':
                    config.configdict["path"] = args[i + 1]
                    i += 1
                case '-s':
                    config.configdict["sort"] = args[i + 1]
                    i += 1
                case '-v':
                    val = args[i + 1].capitalize()
                    if val == "True":
                        config.configdict["verbose"] = True
                    elif val == "False":
                        config.configdict["verbose"] = False
                    else:
                        print(f"ERROR Unknown argument {args[i+1]}")
                    i += 1
                case _:
                    print(f"ERROR Unknown argument {args[i]}")
            i += 1    
    except IndexError:
        print("ERROR Invalid or missing argument")

##########################
# Test program starts here
##########################
if __name__ == "__main__":
    # Execute only if run as a script
    print("Testing...")
    if True:
        read_args(sys.argv)
        print(config.configdict)