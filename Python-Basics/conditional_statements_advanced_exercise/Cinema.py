tickets = input()
rows = int(input())
columns = int(input())
price = 0

capacity = rows * columns

if tickets == "Premiere":
    price = 12
elif tickets == "Normal":
    price = 7.50
elif tickets == "Discount":
    price = 5



print(f"{capacity * price:.2f} leva")


