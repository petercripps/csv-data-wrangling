# Read command line arguments.
import sys
import yaml
from help import print_help

valid_ops = ["wrangle", "list"]

# Reads a list of arguments or, if none, a file in yaml format and returns
# parameters in a dictionary.
# Parameters:
#   args : List - The command line arguments 
# Returns:
#   argdict : dict - A dictionary of values read from the command line 
def read_args(args):    
    argdict = init_argdict()

    # If no arguments see if there is a YAML file
    if len(args) == 1:
        argdict = read_yaml_file("csv-wrangle.yaml")
        print("No arguments provided so using YAML")
    
    # If first argument is -h print help and return empty dict.
    elif args[1] == '-h':
        print_help()
        return {}
    
    # Check if first argument is a valid operation and carry on otherwise
    # first argument is invalid so return an empty dict.
    elif args[1] in valid_ops:
        argdict["operation"] = args[1]
    else:
        print(f"Invalid argument: {args[1]}")
        return {}
    
    # Read remaining arguments starting at second argument
    try:
        i = 2
        while i < len(args):    
            if args[i] == '-i':
                argdict["input"] = args[i + 1]
                i += 1
            elif args[i] == '-o':
                argdict["output"] = args[i + 1]
                i += 1
            else:
                print("Unknown argument", args[i])
            i += 1    
    except IndexError:
        print("Invalid or missing argument")
    return argdict

# Initialise the arguments dictionsary.
# Parameters:
#   None
# Returns:
#   None
def init_argdict():
    return {"operation": "list", # One of: '' | list | wrangle
        "input": "input.csv",
        "output": "wrangled.csv"}

# Reads a file in yaml format.
# Parameters:
#   yfile : String - The file location of the yaml file
# Returns: 
#   data : Dictionary - A dictionary of values read from the yaml file
def read_yaml_file(yfile):
    try:
        with open(yfile) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            if False:
                print(data)
        return data
    except:
        print("YAML file error: ", yfile)
        return {}

##########################
# Test program starts here
##########################
if __name__ == "__main__":
    # execute only if run as a script
    print("Testing...")
    if False:
        args = read_args(sys.argv)
        print(args)