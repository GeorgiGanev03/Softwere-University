locations = int(input())

for location in range(1, locations + 1):
    expected_earn = float(input())
    days = int(input())

    gold = 0

    for day in range(1, days + 1):
        earn = float(input())
        gold += earn

    average_earn = gold / days

    diff_sum = abs(average_earn - expected_earn)

    if average_earn >= expected_earn:
        print(f"Good job! Average gold per day: {average_earn:.2f}.")
    else:
        print(f"You need {diff_sum:.2f} gold.")