# Read command line arguments.
import sys
import yaml
from help import print_help

valid_ops = ["wrangle", "list"]
config_file = "config.yaml"

# Reads a list of arguments or, if none, a file in yaml format and returns
# parameters in a dictionary.
# Parameters:
#   args : List - The command line arguments 
# Returns:
#   dict - A dictionary of values read from the command line 
def read_args(args):
    # Initialise arguments from YAML file    
    configdict = read_yaml_file(config_file)

    if len(args) == 1:
        print("No arguments provided so using YAML")
    
    # If first argument is -h print help and return empty dict.
    elif args[1] == '-h':
        print_help()
        return {}
    
    # Check if first argument is a valid operation and carry on otherwise
    # first argument is invalid so return an empty dict.
    elif args[1] in valid_ops:
        configdict["operation"] = args[1]
    else:
        print(f"Invalid argument: {args[1]}")
        return {}
    
    # Read remaining arguments starting at second argument
    try:
        i = 2
        while i < len(args):    
            if args[i] == '-i':
                configdict["csv-data"] = args[i + 1]
                i += 1
            elif args[i] == '-o':
                configdict["csv-vdata"] = args[i + 1]
                i += 1
            elif args[i] == '-e':
                configdict["csv-edata"] = args[i + 1]
                i += 1
            elif args[i] == '-p':
                configdict["path"] = args[i + 1]
                i += 1
            elif args[i] == '-s':
                configdict["sort"] = args[i + 1]
                i += 1
            else:
                print("Unknown argument", args[i])
            i += 1    
    except IndexError:
        print("Invalid or missing argument")
    return configdict

# Reads a file in yaml format.
# Parameters:
#   yfile : String - The file location of the yaml file
# Returns: 
#   dict - A dictionary of values read from the yaml file
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
    if True:
        args = read_args(sys.argv)
        print(args)