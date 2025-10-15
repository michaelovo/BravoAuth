'''Creating A Login Authentication Program with the Following Requirements:
1. Lastname (String and alphabet only, Not less than 3 characters, must not be empty)
2. Firstname (String and alphabet only, Not less than 3 characters, must not be empty)
3. Email (Must contain @ and . signs, Must not be empty, must have the following
extensions [.net,.org.,.ng])
4.Phone Numbers (Must not be empty, not less than 11digits,accepts numbers only,
must start with [070,080,081,090,091])
5. Gender (list[male,female],string,must not be empty)
6. Address (Must not be empty, minimum of 20 characters)
'''

#Name Authentication Function that validates both firstname and lastname
def name_authentication(name):
    # Check if input is empty
    if not name:
        return False, "Name cannot be empty"
    
    # Check if it's at least 3 characters long
    if len(name) < 3:
        return False, "Name must be minimum of 3 characters"
    
    # Check if it contains only letters (no numbers or symbols)
    if not name.isalpha():
        return False, "Name must contain only alphabets"
    
    # If all checks pass
    return True, "Name is Valid"


#Email Authentication Function - Validates Email Only
def email_authentication(email):
    # Check if empty
    if not email:
        return False,"Email cannot be empty."

    # Check if it contains '@' and '.'
    if "@" not in email or "." not in email:
        return False,"Email must contain both '@' and '.' symbols."

    # Check for extensions (".net",".org",".ng")
    extensions = (".net", ".org", ".ng")
    if not email.endswith(extensions):
        return False, f"Email must end with only extensions: {extensions}."

    # If all checks pass
    return True, "Email is valid!"



