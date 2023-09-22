number = int(input())

name = ""
winner_points = 0

for n in range(1, number + 1):

    total_points = 0

    user = input()
    input_line = input()
    while input_line != "Stop":

        points = int(input_line)
        total_points += points

        input_line = input()

    if total_points >= winner_points:
        name = user
        winner_points = total_points

    print(f"{user} has {total_points} points.")

    if total_points >= winner_points:
        print(f"{name} is the new number 1!")


print(f"{name} won competition with {winner_points} points!")