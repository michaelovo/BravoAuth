def maleGenderValidation(gender):
    if gender == "male":
        return True
    else:
        return False

def femaleGenderValidation(gender):
    if gender == "female":
        return True
    else:
        return False

def get_no_empty_input_from_gender(gender):
    if gender:
        return gender
    else:
        print("Input cannot be empty. Please try again")
