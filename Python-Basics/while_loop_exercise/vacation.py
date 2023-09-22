needed_money = float(input())
available_money = float(input())

total_days = 0
spend_counter = 0

total_sum = available_money
while total_sum < needed_money:

    if spend_counter == 5:
        break

    action = input()
    money = float(input())

    total_days += 1

    if action == "spend":
        total_sum -= money
        spend_counter += 1
        if total_sum < 0:
            total_sum = 0
    else:
        total_sum += money
        spend_counter = 0


if spend_counter == 5:
    print(f"You can't save the money.")
    print(f"{total_days}")
else:
    print(f"You saved the money for {total_days} days.")

