########################################################################
# rules.py
# The rules for validating fields in a CSV.
#######################################################################
import phonenumbers
import math
import config
from datetime import date, datetime
from phonenumbers import geocoder

# Test for required age based on Date of birth (DoB). 
# Valid if current date minus DoB >= age specified.
# Parameters:
#   dob : str - The date of birth to be validated.
#   age : int - age to check
# Returns:
#   bool - True if valid, False otherwise.
def validate_dob(dob, age):
    try:
        # Convert string dob to a datetime object
        born = datetime.strptime(str(dob), '%d/%m/%Y')
        # Convert datetime object to a date object
        born = born.date()
        # Get today's date
        today = date.today()
        # Calculcate age
        calc_age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        if calc_age >= age:
            return True
        else:
            if config.configdict["verbose"]:
                print(f"Invalid DoB {dob} for {age}")
            return False
    except:
        if config.configdict["verbose"]:    
            print(f"ERROR Invalid DoB: {dob}")
        return False

# Test for a valid email. Check it has a '@' and a '.'.
# Parameters:
#   email : str - The email to be validated.
# Returns:
#   bool - True if valid, False otherwise.
def validate_email(email):
    if (email.find('@') == -1) or (email.find('.') == -1):
        if config.configdict["verbose"]:
            print(f"Invalid email: {email}")
        return False
    return True

# Test for a valid university. Check it is in list of valid universities'.
# Parameters:
#   uni : str - The university to be validated.
# Returns:
#   bool - True if valid, False otherwise.
def validate_uni(uni): 
    uni = str(uni).replace(" ", "")
    if (uni in config.configdict['unilist']):
        return True
    else:
        if config.configdict["verbose"]:
            print(f"Invalid university: {uni}")
        return False

# Test for a valid phone number.
# Parameters:
#   num : str - The number to be validated.
# Returns:
#   bool - True if valid, False otherwise.
def validate_phonenum(num):
    try:
        # First remove whitespace.
        num = num.replace(" ", "")
        # If starts with '0' and 11 digits valid in UK
        if ((num[0] == '0') and (len(num) == 11)):
            return True
        # If start with '7' and 10 digits valid in UK    
        elif ((num[0] == '7') and (len(num) == 10)):
            return True
        # If start with '+' check for international numbers    
        elif (num[0] == '+'):
            return (validate_int(num))   
        if config.configdict["verbose"]:
            print(f"Invalid phone number: {num}")
        return False
    except:
        if config.configdict["verbose"]:
            print(f"ERROR Invalid phone number {num}")
        return False

# Test for a valid country code.
# Check this library: https://stackabuse.com/validating-and-formatting-phone-numbers-in-python/ 
# Parameters:
#   snum : str - The number to be validated (stripped of spaces).
# Returns:
#   bool - True if valid, False otherwise.
def validate_int(snum):
    return True

# Test for a valid phone number using the Python package 'Phonenumbers'. 
# Parameters:
#   num : str - The number to be validated.
#   cc : valid ISO country code
# Returns:
#   bool - True if valid, False otherwise.
def validate_phonenum_pn(num, cc):
    try:
        parsed_num = phonenumbers.parse(num, cc)
        return phonenumbers.is_valid_number(parsed_num)
    except:
        if config.configdict["verbose"]:
            print(f"ERROR Invalid number: {num} or CC {cc}")
        return False    
    
##########################
# Test program starts here
##########################
if __name__ == "__main__":
    # execute only if run as a script
    print("Testing...")
    use_pn_pkg = False
    if config.configdict["verbose"]:
        row = ['joe@gmail.com',"07016730224","UCL","28/05/2004"]

        if use_pn_pkg:
            print(f"Mobile {row[1]} valid (using pn) = {validate_phonenum_pn(row[1],'GB')}")
        else:
            print(f"Mobile {row[1]} valid = {validate_phonenum(row[1])}")        
        print(f"Email {row[0]} valid = {validate_email(row[0])}")
        print(f"University {row[2]} valid = {validate_uni(row[2])}")
        print(f"DoB {row[3]} valid = {validate_dob(row[3],22)}")