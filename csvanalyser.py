########################################################################
# csvanalyser.py
# Entry point for command line version of CSV data analysis program. 
# Ensure these packages are installed using pip3:
# pip3 install numpy
# pip3 install pandas
# pip3 install phonenumbers
# pip3 install pyyaml
# (Check what's installed using 'pip3 list')
########################################################################

import pandas as pd
import numpy as np
import sys
import csv
import config
from readargs import read_args
from rules import validate_dob, validate_email, validate_uni, validate_phonenum, validate_uniyear, validate_phonenum_ext

# Start the program having loaded up parameters into config.configdict.
# Parameters:
#   None 
# Returns:
#   None
def run_csv_analyse():
    try:
        if config.configdict != {}:
            if config.configdict["operation"] == "analyse":
                if config.configdict["csv-edata"] == "":
                    csv_analyse()
                    print(f"Output in {config.configdict['csv-vdata']}")
                else:
                    csv_analyse_split()
                    print(f"Output in {config.configdict['csv-vdata']} and {config.configdict['csv-edata']}")
            elif config.configdict["operation"] == "list":
                csv_list()
            else:
                print(__file__, f"ERROR Invalid operation: {config.configdict['operation']}")
    except KeyError:
        print(__file__, "ERROR Missing key in YAML file")

# Analyse a CSV file according to a set of rules. Read the CSV into a new Pandas DataFrame, create
# two additional DataFrames, one for valid rows in the CSV and another for invalid rows. Also set the
# column names to shorter nouns which will be used for indexing. These can be changed in the YAML
# but, for now, will need to be modified in code as they are currently hardcoded.
# Parameters:
#   None 
# Returns:
#   None
def csv_analyse_split():
    try:
        # Read CSV data as a panda dataframe. Use dtype=object to preserve and not interpret dtype
        df1 = pd.read_csv(config.configdict["path"] + config.configdict["csv-data"],dtype=object)

        # Rename columns to make more manageable (names are in config yaml)
        col_names = config.configdict["col_names"]
        df1.columns = col_names

        # Iterate through CSV a row at a time and check contents of each column applying approriate rules.
        # If the row is valid add it to the validated dataframe, if one or more fields are invalid add to
        # an invalid dataframe.
        i = 0
        valid_df = pd.DataFrame(columns = col_names)
        # Invalid DF will have extra column indicating error
        col_names.append("Error")
        invalid_df = pd.DataFrame(columns = col_names)
        # j is index for error file
        j = 0
        while i < len(df1):
            vrow = validate_row(i, df1.loc[i])
            if vrow[1] == "":
                valid_df.loc[len(valid_df)] = vrow[0]
            else:
                invalid_df.loc[len(invalid_df)] = vrow[0]
                invalid_df.at[j, 'Error'] = vrow[1]
                j += 1
            i += 1
        # Sort the output files if sort parameter defined
        if config.configdict['sort'] != "":
            valid_df = csv_sort(config.configdict['sort'], valid_df)
            invalid_df = csv_sort(config.configdict['sort'], invalid_df)
        # When done write out the valid and invalid dataframes as CSV files.
        valid_df.to_csv(config.configdict["path"] + config.configdict["csv-vdata"], index=False)
        invalid_df.to_csv(config.configdict["path"] + config.configdict["csv-edata"], index=False)
    except IsADirectoryError:
        print(__file__, f"ERROR Invalid path or file")
    except FileNotFoundError:
        print(__file__, f"ERROR Invalid file")

# Analyse a CSV file according to a set of rules. Read the CSV into a new Pandas DataFrame, create
# an additional DataFrame for writing validated rows in the CSV with an additional column indicating
# which cells are in error. Also set the column names to shorter nouns which will be used for indexing.
# These can be changed in the YAML but, for now, will need to be modified in code as they are currently
# hardcoded.
# Parameters:
#   None 
# Returns:
#   None
def csv_analyse():
    try:
        # Read CSV data as a panda dataframe. Use dtype=object to preserve and not interpret dtype
        df1 = pd.read_csv(config.configdict["path"] + config.configdict["csv-data"],dtype=object)

        # Rename columns to make more manageable (names are in config yaml)
        col_names = config.configdict["col_names"]
        df1.columns = col_names

        # Iterate through CSV a row at a time and check contents of each column applying approriate rules.
        # If the row is valid add it to the validated dataframe, if one or more fields are invalid add to
        # an invalid dataframe.
        i = 0
        col_names.append("Error")
        output_df = pd.DataFrame(columns = col_names)
        while i < len(df1):
            vrow = validate_row(i, df1.loc[i])
            output_df.loc[len(output_df)] = vrow[0]
            output_df.at[i, 'Error'] = vrow[1]
            i += 1
        # Sort the output file if sort parameter defined
        if config.configdict['sort'] != "":
            output_df = csv_sort(config.configdict['sort'], output_df)
        # When done write out the output dataframe as a CSV files.
        output_df.to_csv(config.configdict["path"] + config.configdict["csv-vdata"], index=False)
    except IsADirectoryError:
        print(__file__, f"ERROR Invalid path or file")
    except FileNotFoundError:
        print(__file__, f"ERROR Invalid file")

# Validate a single row from a dataframe using approriate rules. Note the indexes used in the rules
# will need updating here if they are changed in the config YAML. A rule is only run if the flag for that rule
# in the YAML dictionary 'rules' is 'True'.
# Parameters:
#   rownum : Integer - Number of row in file
#   row : Series - The row containing the elements to be validated.
# Returns:
#   list - A list whose first element is a Series and whose second element is a String indicating if
#   the series has any invalid cells (and what they are).
def validate_row(rownum, row):
    # Define a null string to contain error codes, will stay as null if no errors
    err_str = ""
    # Run the rules one by one, if error record in err_str
    if (config.configdict["rules"]["DOB"]):
        if not validate_dob(row["DOB"],18):
            err_str = err_str + "DOB "
    if (config.configdict["rules"]["Email"]):
        if not validate_email(row["Email"]):
            err_str = err_str + "Email "
    if (config.configdict["rules"]["Uni"]):
        if not validate_uni(row["Uni"]):
            err_str = err_str + "Uni "
    if (config.configdict["rules"]["Mobile"]):
        if not validate_phonenum(row["Mobile"]):
            err_str = err_str + "Mobile "
    if (config.configdict["rules"]["MobileExt"]):
        if not validate_phonenum_ext(row["Mobile"],'GB'):
            err_str = err_str + "MobileExt "
    if (config.configdict["rules"]["UniYear"]):
        if not validate_uniyear(row["UniYear"]):
            err_str = err_str + "UniYear"

    return [row, err_str]

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
        print(__file__, f"ERROR Invalid key {sort_by}")
    return df

# List a CSV file.
# Parameters:
#   None 
# Returns:
#   None
def csv_list():
    try:
        # Read CSV data as a panda dataframe
        df1 = pd.read_csv(config.configdict["path"] + config.configdict["csv-data"])
        # Rename columns to make more manageable (names are also in config yaml)
        col_names = config.configdict["col_names"]
        df1.columns = col_names
        # Print the DF
        print(df1)
    except FileNotFoundError:
        print(__file__, f"ERROR Invalid file {config.configdict['csv-data']} or path {config.configdict['path']}")
    

############################
# Main program starts here #
############################
if __name__ == "__main__":
    # Read command line args and take action depending on the 'operation' 
    # entry of the returned dictionary.
    read_args(sys.argv)
    # Run the main program
    run_csv_analyse()