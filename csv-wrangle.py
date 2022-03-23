# Entry point for command line version of CSV data wrangling program. 
# Ensure these packages are installed using pip3:
# pip3 install numpy
# pip3 install pandas
# Check using 'pip3 list'

import pandas as pd
import numpy as np
import sys
import csv
from readargs import read_args, read_yaml_file
from rules import validate_dob, validate_email, validate_uni

config_file = "config.yaml"
col_names = ['Lname', 'Fname', 'Email', 'OptOut', 'TicketType', 'OrderDate', 'OrderRef', 'RepName', 'RepEmail', 'Confirm', 'DOB', 'Mobile', 'Uni']

# Start the program having loaded up parameters into argdict.
# Parameters:
#   argdict : Dictionary - A dictionary of values read from the command line 
# Returns:
#   None
def run_csv_wrangle(argdict):
    if argdict != {}:
        if argdict["operation"] == "wrangle":
            csv_wrangle()
        elif argdict["operation"] == "list":
            csv_list()
        else:
            print(__file__, "Invalid operation: ", argdict["operation"])

# Wrangle a CSV file according to a set of rules.
# Parameters:
#   None 
# Returns:
#   List - A list containing the valid df as the first element and invalid df as the second
def csv_wrangle():
    print("Wrangling data")
    configdict = read_yaml_file(config_file)
    try:
        # Read CSV data as a panda dataframe
        df1 = pd.read_csv(configdict["path"] + configdict["csv-data"])

        # Rename columns to make more manageable
        df1.columns = col_names

        # Iterate through CSV a row at a time and check contents of each column applying approriate rules.
        # If the row is valid add it to the validated dataframe, if one or more fields are invalid add to
        # an invalid dataframe.
        i = 0
        valid_df = pd.DataFrame(columns = col_names)
        invalid_df = pd.DataFrame(columns = col_names)
        while i < len(df1):
            vrow = validate_row(df1.loc[i])
            if vrow[1]:
                valid_df.loc[len(valid_df)] = vrow[0]
            else:
                invalid_df.loc[len(invalid_df)] = vrow[0]
            i += 1

    except FileNotFoundError:
        print(__file__, "Invalid file or path")
    return [valid_df,invalid_df]

# Validate a single row from a dataframe using approriate rules.
# Parameters:
#   row : Series - The row containing the elements to be validated. 
# Returns:
#   List - A list whose first element is a Series and whose second element is a Boolean indicating if the series has any invalid elements.
def validate_row(row):
    # Assume valid until proven otherwise.
    is_valid = True 
    is_valid = validate_dob(row['DOB'])
    is_valid = validate_email(row['Email'])
    is_valid = validate_uni(row['Uni'])
    
    # Return the row and if it is valid or not as a List.
    return [row, is_valid]

# List a CSV file.
#   None 
# Returns:
#   None
def csv_list():
    print("Listing data")
    

############################
# Main program starts here #
############################
if __name__ == "__main__":

    # Read command line args and take action depending on the 'operation' 
    # entry of the returned dictionary.
    argdict = read_args(sys.argv)
    run_csv_wrangle(argdict)