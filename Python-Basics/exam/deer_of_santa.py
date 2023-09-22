import math

days_its_gone = int(input())
food_left_kg = int(input())
food_for_deer1 = float(input())
food_for_deer2 = float(input())
food_for_deer3 = float(input())

food_for_deer1 = food_for_deer1 * days_its_gone
food_for_deer2 = food_for_deer2 * days_its_gone
food_for_deer3 = food_for_deer3 * days_its_gone

total_food = food_for_deer1 + food_for_deer2 + food_for_deer3

diff_sum = abs(food_left_kg - total_food)

if total_food < food_left_kg:
    print(f"{math.floor(diff_sum)} kilos of food left.")
else:
    print(f"{math.ceil(diff_sum)} more kilos of food are needed.")