budget = int(input())
season = input()
fisherman = int(input())

price = 0

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if fisherman <= 6:
    price = price * 0.9
elif 6 < fisherman <= 11:
    price = price * 0.85
elif fisherman > 11:
    price = price * 0.75

if fisherman % 2 == 0 and season != "Autumn":
    price = price * 0.95

final_price = abs(price - budget)

if budget >= price:
    print(f"Yes! You have {final_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {final_price:.2f} leva.")




