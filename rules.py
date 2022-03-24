# The rules for validating fields in a CSV

def validate_dob(dob):
    return True

# Test for a valid email. Check it has a '@' and a '.'.
# Parameters:
#   email : str - The email to be validated.
# Returns:
#   bool - True if valid, False otherwise.
def validate_email(email):
    if (email.find('@') == -1) or (email.find('.') == -1):
        print(f"Invalid email: {email}")
        return False
    return True

def validate_uni(uni):
    return True

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

##########################
# Test program starts here
##########################
if __name__ == "__main__":
    # execute only if run as a script
    print("Testing...")
    if True:
        print("Mobile valid: ", validate_phonenum('07801673022'))
        print("Email valid: ", validate_email('joe@gmail.com'))