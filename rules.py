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
