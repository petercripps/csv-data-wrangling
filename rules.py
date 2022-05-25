import phonenumbers
import math
from datetime import date, datetime
from phonenumbers import geocoder
from readargs import read_yaml_file

# The rules for validating fields in a CSV

# Set this to True to get debug info out of rules
debug = False

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
        if debug:
            print(f"DoB: {born} age: {calc_age}")
        return calc_age >= age
    except:
        print(f"Invalid date {dob}")
        return False

# Test for a valid email. Check it has a '@' and a '.'.
# Parameters:
#   email : str - The email to be validated.
# Returns:
#   bool - True if valid, False otherwise.
def validate_email(email):
    if (email.find('@') == -1) or (email.find('.') == -1):
        if debug:
            print(f"Invalid email: {email}")
        return False
    return True

# Test for a valid university. Check it is in list of valid universities'.
# Parameters:
#   uni : str - The university to be validated.
#   unilist : str - The list of universities to be checked against.
# Returns:
#   bool - True if valid, False otherwise.
def validate_uni(uni, unilist): 
    uni = str(uni).replace(" ", "")
    if (uni in unilist):
        return True
    else:
        if debug:
            print(f"Invalid university: {uni}")
        return False

# Test for a valid phone number.
# Parameters:
#   num : str - The number to be validated.
# Returns:
#   bool - True if valid, False otherwise.
def validate_phonenum(num):
    try:
        # Now ensure the number is first an int then a str
        num = str(int(num))
        # Now remove whitespace.
        snum = num.replace(" ", "")
        # If starts with '0' and 11 digits valid in UK
        if ((snum[0] == '0') and (len(snum) == 11)):
            return True
        # If start with '7' and 10 digits valid in UK    
        elif ((snum[0] == '7') and (len(snum) == 10)):
            return True
        # If start with '+' check for international numbers    
        elif (snum[0] == '+'):
            return (validate_int(snum))
        if debug:    
            print(f"Invalid number: {num}")
        return False
    except:
        print(f"Invalid phone num {num}")
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
        print(f"Invalid number: {num} or CC {cc}")
        return False    
    
##########################
# Test program starts here
##########################
if __name__ == "__main__":
    # execute only if run as a script
    print("Testing...")
    use_pn_pkg = True
    if debug:
        row = ['joe@gmail.com',"07801673022","UCL","12/05/2001"]
        configdict = read_yaml_file("config.yaml")

        if use_pn_pkg:
            print(f"Mobile {row[1]} valid (using pn) = {validate_phonenum_pn(row[1],'GB')}")
        else:
            print(f"Mobile {row[1]} valid = {validate_phonenum(row[1])}")        
        print(f"Email {row[0]} valid = {validate_email(row[0])}")
        print(f"University {row[2]} valid = {validate_uni(row[2],configdict['unilist'])}")
        print(f"DOB {row[3]} valid = {validate_dob(row[3],22)}")