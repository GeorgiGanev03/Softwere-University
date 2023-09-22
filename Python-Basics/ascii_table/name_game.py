name = ""
total_points = 0

input_line = input()
while input_line != "Stop":

    points = 0

    for letter in input_line:
        number = int(input())
        letter_counter = 0

        letter_counter += ord(letter)

        if letter_counter == number:
            points += 10
        else:
            points += 2

    if points >= total_points:
        name = input_line
        total_points = points
    else:
        break

    input_line = input()

print(f"The winner is {name} with {total_points} points!")
