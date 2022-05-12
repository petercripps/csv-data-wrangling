import phonenumbers
from phonenumbers import geocoder

# The rules for validating fields in a CSV

# Set this to True to get debug info out of rules
debug = False

def validate_dob(dob):
    return True

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
    if uni in unilist:
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
    # Remove whitespace first.
    snum = num.replace(" ", "")
    # If start with '0' and 11 digits valid in UK
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
        parsed_num = phonenumbers.parse(test_num, cc)
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
        test_num = '+107801674567'
        test_email = 'joe@gmail.com'
        test_uni = "University of Birmingham"

        if use_pn_pkg:
            print("Mobile valid (using pn): ", validate_phonenum_pn(test_num, 'GB'))
        else:
            print("Mobile valid: ", validate_phonenum(test_num))        
        print("Email valid: ", validate_email('joe@gmail.com'))
        print("University valid: ", validate_uni(test_uni))