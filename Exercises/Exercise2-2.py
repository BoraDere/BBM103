mail = input("Please provide an email address: ")
requiredCharacters = "@."
for element in mail:
    if requiredCharacters in mail:
        print("This is a valid email address.")
        break
    else:
        print("This is an invalid email address.")