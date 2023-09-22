days = int(input())
type_of_room = input()
grade = input()

days = days - 1

price = 0

if type_of_room == "room for one person":
    price = 18 * days
elif type_of_room == "apartment":
    price = 25 * days

    if days < 10:
        price = price * 0.70
    elif 10 < days < 15:
        price = price * 0.65
    elif days > 15:
        price = price * 0.50
elif type_of_room == "president apartment":
    price = 35 * days

    if days < 10:
        price = price * 0.90
    elif 10 < days < 15:
        price = price * 0.85
    elif days > 15:
        price = price * 0.80

discount_positive = price * 0.25
discount_negative = price * 0.10

if grade == "positive":
    price = price + discount_positive
else:
    price = price - discount_negative

print(f"{price:.2f}")