def validate_first_name(first_name):
    if isinstance(first_name, str) and len(first_name) >= 3 and first_name.isalpha():
        return True
    return False

def validate_last_name(last_name):
    if isinstance(last_name, str) and len(last_name) >= 3 and last_name.isalpha():
        return True
    return False