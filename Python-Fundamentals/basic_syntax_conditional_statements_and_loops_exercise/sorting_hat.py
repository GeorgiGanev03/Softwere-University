input_line = input()

while True:
    if input_line == "Welcome!":
        print(f"Welcome to Hogwarts.")
        break
    elif input_line == "Voldemort":
        print(f"You must not speak of that name!")
        break

    if len(input_line) < 5:
        print(f"{input_line} goes to Gryffindor.")
    elif len(input_line) == 5:
        print(f"{input_line} goes to Slytherin.")
    elif len(input_line) == 6:
        print(f"{input_line} goes to Ravenclaw.")
    elif len(input_line) > 6:
        print(f"{input_line} goes to Hufflepuff.")

    input_line = input()