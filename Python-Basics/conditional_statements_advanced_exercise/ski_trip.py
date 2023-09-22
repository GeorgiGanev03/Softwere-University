days_for_stay = int(input())
room = input()
grade = input()

price = 0
if days_for_stay >= 1:
    days_for_stay = days_for_stay - 1

if room == "room for one person":
    price = 18
elif room == "apartment":
    price = 25
elif room == "president apartment":
    price = 35

days = days_for_stay * price

if room == "apartment":
    if days_for_stay < 10:
        days = days * 0.7
    elif 10 < days_for_stay < 15:
        days = days * 0.65
    elif days_for_stay > 15:
        days = days * 0.5
elif room == "president apartment":
    if days_for_stay < 10:
        days = days * 0.9
    elif 10 < days_for_stay < 10:
        days = days * 0.85
    elif days_for_stay > 15:
        days = days * 0.8

if grade == "positive":
    days = days * 1.25
elif grade == "negative":
    days = days * 0.9


print(f"{days:.2f}")



