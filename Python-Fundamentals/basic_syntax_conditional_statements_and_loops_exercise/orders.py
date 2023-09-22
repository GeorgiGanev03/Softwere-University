n = int(input())

total_price = 0

for day in range(1, n + 1):

    price = float(input())
    days = int(input())
    capsules = int(input())

    coffee_price = price * days * capsules

    if coffee_price == 0:
        continue

    if 0.01 <= price <= 100.00 and 1 <= days <= 31 and 1 <= capsules <= 2000:

        total_price += coffee_price

        print(f"The price for the coffee is: ${coffee_price:.2f}")

print(f"Total: ${total_price:.2f}")
