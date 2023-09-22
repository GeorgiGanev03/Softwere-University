target_per_day = int(input())

price = 0

input_line = input()
while input_line != "closed":
    customer = input()

    if input_line == "haircut":
        if customer == "mens":
            price += 15
        elif customer == "ladies":
            price += 20
        elif customer == "kids":
            price += 10

    elif input_line == "color":
        if customer == "touch up":
            price += 20
        elif customer == "full color":
            price += 30

    if price >= target_per_day:
        break

    input_line = input()

diff_sum = abs(target_per_day - price)
if price >= target_per_day:
    print(f"You have reached your target for the day!" )
    print(f"Earned money: {price}lv.")
else:
    print(f"Target not reached! You need {diff_sum}lv. more.")
    print(f"Earned money: {price}lv.")