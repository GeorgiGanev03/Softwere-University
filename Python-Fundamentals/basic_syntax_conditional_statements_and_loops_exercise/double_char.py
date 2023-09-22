input_line = input()
while input_line != "End":

    new_string = ""

    if input_line != "SoftUni":

        for letter in input_line:
            new_string += letter * 2
        print(new_string)

    input_line = input()







