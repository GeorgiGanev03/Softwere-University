food = input()
day = input()
quantity = int(input())
price = 0

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if food == "banana":
        price = 2.50
    elif food == "apple":
        price = 1.20
    elif food == "orange":
        price = 0.85
    elif food == "grapefruit":
        price = 1.45
    elif food == "kiwi":
        price = 2.70
    elif food == "pineapple":
        price = 5.50
    elif food == "grapes":
        price = 3.85

    print(f"{quantity * price:.2f}")

elif day == "Saturday" or day == "Sunday":
    if food == "banana":
        price = 2.70
    elif food == "apple":
        price = 1.25
    elif food == "orange":
        price = 0.90
    elif food == "grapefruit":
        price = 1.60
    elif food == "kiwi":
        price = 3.00
    elif food == "pineapple":
        price = 5.60
    elif food == "grapes":
        price = 4.20

    print(f"{quantity * price:.2f}")

else:
    print("error")