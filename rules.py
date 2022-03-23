# The rules for validating fields in a CSV

def validate_dob(dob):
    return True

# Test for a valid email. Check it has a '@' and a '.'.
# Parameters:
#   email : str - The email to be validated.
# Returns:
#   bool
def validate_email(email):
    if (email.find('@') == -1) or (email.find('.') == -1):
        print(f"Invalid email: {email}")
        return False
    return True

def validate_uni(uni):
    return True

# Test for a valid mobile. Check it has a '0' or a '7' to start and is 11 or 10 digits.
# Parameters:
#   mobile : str - The mobile to be validated.
# Returns:
#   bool
def validate_mobile(mobile):
    # Remove whitespace first.
    smobile = mobile.replace(" ", "")
    if ((smobile[0] == '0') and (len(smobile) == 11)):
        return True
    elif ((smobile[0] == '7') and (len(smobile) == 10)):
        return True
    print(f"Invalid mobile: {mobile}")
    return False

##########################
# Test program starts here
##########################
if __name__ == "__main__":
    # execute only if run as a script
    print("Testing...")
    if False:
        print("Mobile valid: ", validate_mobile('07801673022'))
        print("Email valid: ", validate_email('joe@gmail.com'))