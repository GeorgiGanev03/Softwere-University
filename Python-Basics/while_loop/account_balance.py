account_balance = 0

while True:
    deposit = input()

    if deposit == "NoMoreMoney":
        break

    current_number = float(deposit)

    if current_number >= 0:
        account_balance += current_number
        print(f"Increase: {current_number:.2f}")

    else:
        print(f"Invalid operation!")
        break

print(f"Total: {account_balance:.2f}")
