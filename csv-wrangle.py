# Entry point for command line version of CSV data wrangling program. 
# Ensure these packages are installed using pip3:
# pip3 install numpy
# pip3 install pandas
# pip3 install phonenumbers
# Check using 'pip3 list'

import pandas as pd
import numpy as np
import sys
import csv
from readargs import read_args, read_yaml_file
from rules import validate_dob, validate_email, validate_uni, validate_phonenum

# Start the program having loaded up parameters into configdict.
# Parameters:
#   configdict : Dictionary - A dictionary of values read from the command line or config.yaml 
# Returns:
#   None
def run_csv_wrangle(configdict):
    if configdict != {}:
        if configdict["operation"] == "wrangle":
            csv_wrangle(configdict)
        elif configdict["operation"] == "list":
            csv_list(configdict)
        else:
            print(__file__, "Invalid operation: ", configdict["operation"])

# Wrangle a CSV file according to a set of rules. Read the CSV into a new Pandas DataFrame, create
# two additional DataFrames, one for valid rows in the CSV and another for invalid rows. Also set the
# column names to shorter nouns which will be used for indexing. These can be changed in the YAML
# but, for now, will need to be modified in code as they are currently hardcoded.
# Parameters:
#   configdict : Dictionary - A dictionary of values read from the command line or config.yaml 
# Returns:
#   list - A list containing the valid df as the first element and invalid df as the second
def csv_wrangle(configdict):
    try:
        # Read CSV data as a panda dataframe
        df1 = pd.read_csv(configdict["path"] + configdict["csv-data"])

        # Rename columns to make more manageable (names are also in config yaml)
        col_names = configdict["col_names"]
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

# Validate a single row from a dataframe using approriate rules. Note the indexes used in the rules
# will need updating here if they are changed in the config YAML.
# Parameters:
#   row : Series - The row containing the elements to be validated. 
# Returns:
#   list - A list whose first element is a Series and whose second element is a Boolean indicating if the series has any invalid elements.
def validate_row(row):
    # Assume valid until proven otherwise.
    is_valid = True 
    is_valid = validate_dob(row['DOB'])
    is_valid = validate_email(row['Email'])
    is_valid = validate_uni(row['Uni'])
    is_valid = validate_phonenum(str(row['Mobile']))
    
    # Return the row and if it is valid or not as a List.
    return [row, is_valid]

# List a CSV file.
# Parameters:
#   configdict : Dictionary - A dictionary of values read from the command line or config.yaml 
# Returns:
#   None
def csv_list(configdict):
    try:
        # Read CSV data as a panda dataframe
        df1 = pd.read_csv(configdict["path"] + configdict["csv-data"])

        # Rename columns to make more manageable (names are also in config yaml)
        col_names = configdict["col_names"]
        df1.columns = col_names

        # Print the DF
        print(df1)

    except FileNotFoundError:
        print(__file__, "Invalid file or path")
    

############################
# Main program starts here #
############################
if __name__ == "__main__":

    # Read command line args and take action depending on the 'operation' 
    # entry of the returned dictionary.
    configdict = read_args(sys.argv)
    run_csv_wrangle(configdict)