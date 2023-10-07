def is_not_valid(password: str) -> list:
    errors_list = []

    if len(password) < 6 or len(password) > 10:
        errors_list.append(f"Password must be between 6 and 10 characters")
    if not password.isalnum():
        errors_list.append(f"Password must consist only of letters and digits")
    counter = 0
    for number in password:
        if number.isdigit():
            counter += 1
    if counter < 2:
        errors_list.append(f"Password must have at least 2 digits")

    return errors_list


password = input()

invalid = is_not_valid(password)
if not invalid:
    print(f"Password is valid")
else:
    print(*is_not_valid(password), sep="\n")




