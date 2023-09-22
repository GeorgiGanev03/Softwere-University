input_line = input()

counter = 0
while input_line != "END":

    if input_line.lower() == "coding" or input_line.lower() == "dog" \
        or input_line.lower() == "cat" \
        or input_line.lower() == "movie":

        if input_line.islower():
            counter += 1
        else:
            counter += 2

    input_line = input()

if counter > 5:
    print(f"You need extra sleep")
else:
    print(counter)