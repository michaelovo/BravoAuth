import first_lastname

print("Enter your first name:")
first_name = input()
print("Enter your last name:")
last_name = input()

if first_lastname. validate_first_name(first_name) == True and first_lastname. validate_last_name(last_name) == True:
    print("Both names are valid!")
else:
    print("Invalid name(s) entered.")