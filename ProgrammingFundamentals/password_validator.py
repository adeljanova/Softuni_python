def is_valid(password):
    digit_counter = 0
    is_valid = False
    if counter < 6 or counter > 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")
    else:
        is_valid = True
    for item in range(len(password)):
        if password[item] < chr(48) or chr(57) < password[item] < chr(65) \
                or chr(90) < password[item] < chr(97) or password[item] > chr(122):
            print("Password must consist only of letters and digits")
            is_valid = False
            break
        else:
            is_valid = True
    for item in range(len(password)):
        temp_symbol = password[item]
        if chr(48) <= temp_symbol <= chr(57):
            digit_counter += 1
    if digit_counter >= 2 and is_valid:
        print("Password is valid")
    else:
        print("Password must have at least 2 digits")


generated_password = input()
counter = 0
for i in range(len(generated_password)):
    counter += 1

is_valid(generated_password)