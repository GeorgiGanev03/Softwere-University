flowers = input()
number_of_flowers = int(input())
budget = int(input())

price = 0

if flowers == "Roses":
    price = 5 * number_of_flowers
    if number_of_flowers > 80:
        price = price * 0.80
elif flowers == "Dahlias":
    price = 3.80 * number_of_flowers
    if number_of_flowers > 90:
        price = price * 0.85
elif flowers == "Tulips":
    price = 2.80 * number_of_flowers
    if number_of_flowers > 80:
        price = price * 0.85
elif flowers == "Narcissus":
    price = 3 * number_of_flowers
    if number_of_flowers < 120:
        price = price * 1.15
elif flowers == "Gladiolus":
    price = 2.50 * number_of_flowers
    if number_of_flowers < 80:
        price = price * 1.20


final_price = abs(price - budget)

if price <= budget:
    print(f"Hey, you have a great garden with {number_of_flowers} {flowers} and {final_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {final_price:.2f} leva more.")