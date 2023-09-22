budget = float(input())
season = input()

location = ""
destination = ""
price = 0

if budget <= 100:
    location = "Bulgaria"
    if season == "summer":
        destination = "Camp"
        price = budget - (budget * 0.70)
    elif season == "winter":
        destination = "Hotel"
        price = budget - (budget * 0.30)

elif budget <= 1000:
    location = "Balkans"
    if season == "summer":
        destination = "Camp"
        price = budget - (budget * 0.60)
    elif season == "winter":
        destination = "Hotel"
        price = budget - (budget * 0.20)

elif budget > 1000:
    location = "Europe"
    if season == "summer" or season == "winter":
        destination = "Hotel"
        price = budget - (budget * 0.10)


print(f"Somewhere in {location}")
print(f"{destination} - {price:.2f}")