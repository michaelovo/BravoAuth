import AuthenticationValidators

print("Enter your first name:")
first_name = input()
print("Enter your last name:")
last_name = input()

if AuthenticationValidators. validate_first_name(first_name) == True and AuthenticationValidators. validate_last_name(last_name) == True:
    print("Both names are valid!")
else:
    print("Invalid name(s) entered.")

address = input("Enter your address: ")

if AuthenticationValidators.check_address(address)== True:
    print("Address accepted:", address)
else:
    print("Error: Address must be at least 20 characters long.")