tournaments = int(input())
starting_points = int(input())

total_points = 0
number_of_wins = 0

for n in range(1, tournaments+1):
    number_tournament = input()

    if number_tournament == "W":
        total_points += 2000
        number_of_wins += 1
    elif number_tournament == "F":
        total_points += 1200
    elif number_tournament == "SF":
        total_points += 720

points = total_points + starting_points

average_points = int(total_points / tournaments)

winning_tournament_percent = number_of_wins / tournaments * 100

print(f"Final points: {points}")
print(f"Average points: {average_points}")
print(f"{winning_tournament_percent:.2f}%")