import AuthenticationValidators
gender = str(input("Ender gender :")).lower()
if AuthenticationValidators.get_no_empty_input_from_gender(gender) == gender:
    if AuthenticationValidators.maleGenderValidation(gender) == True or AuthenticationValidators.femaleGenderValidation(gender) == True:
        print("Congratulation!!!")
    else:
        print("Try Again")
