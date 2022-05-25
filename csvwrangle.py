# Entry point for command line version of CSV data wrangling program. 
# Ensure these packages are installed using pip3:
# pip3 install numpy
# pip3 install pandas
# pip3 install phonenumbers
# pip3 install pyyaml
# Check using 'pip3 list'

import pandas as pd
import numpy as np
import sys
import csv
from readargs import read_args, read_yaml_file
from rules import validate_dob, validate_email, validate_uni, validate_phonenum

# Set this to True to get debug info out of this file
debug = False

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
    valid_df = pd.DataFrame()
    invalid_df = pd.DataFrame()
    try:
        # Read CSV data as a panda dataframe
        df1 = pd.read_csv(configdict["path"] + configdict["csv-data"])

        # Rename columns to make more manageable (names are in config yaml)
        col_names = configdict["col_names"]
        df1.columns = col_names

        # Iterate through CSV a row at a time and check contents of each column applying approriate rules.
        # If the row is valid add it to the validated dataframe, if one or more fields are invalid add to
        # an invalid dataframe.
        i = 0
        valid_df = pd.DataFrame(columns = col_names)
        invalid_df = pd.DataFrame(columns = col_names)
        while i < len(df1):
            vrow = validate_row(i, df1.loc[i], configdict)
            if vrow[1]:
                valid_df.loc[len(valid_df)] = vrow[0]
            else:
                invalid_df.loc[len(invalid_df)] = vrow[0]
            i += 1
        # sort the output files if sort parameter defined
        if configdict['sort'] != "":
            valid_df = csv_sort(configdict['sort'], valid_df)
            invalid_df = csv_sort(configdict['sort'], invalid_df)
        # When done write out the valid and invalid dataframes as CSV files.
        valid_df.to_csv(configdict["path"] + configdict["csv-vdata"], index=False)
        invalid_df.to_csv(configdict["path"] + configdict["csv-edata"], index=False)
    except FileNotFoundError:
        print(__file__, "Invalid file or path")
    return [valid_df,invalid_df]

# Validate a single row from a dataframe using approriate rules. Note the indexes used in the rules
# will need updating here if they are changed in the config YAML.
# Parameters:
#   rownum : Integer - Number of row in file
#   row : Series - The row containing the elements to be validated. 
#   configdict : Dict - Dictionary of config parameters.
# Returns:
#   list - A list whose first element is a Series and whose second element is a Boolean indicating if the series has any invalid elements.
def validate_row(rownum, row, configdict):
    # Run the rules one by one
    if (validate_dob(row["DOB"],18) and 
        validate_email(row["Email"]) and 
        validate_email(row["Email"]) and 
        validate_uni(row["Uni"], configdict["unilist"]) and 
        validate_phonenum(row["Mobile"])):
        return [row, True]
    else:
        if debug:
            print(f"Row {rownum} is invalid")
        return [row, False]

# Sort a DataFrame
# Parameters
#   sort_by: String - Column name to be sorted by
#   df: DataFrame - DataFrame to be sorted
# Returns:
#   DataFrame - Sorted DataFrame
def csv_sort(sort_by, df):
    try:
        df.sort_values(by=[sort_by], inplace=True)
    except KeyError:
        print(__file__, "Invalid key: ", sort_by)
    return df

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