food_kg = int(input())

food_gr = food_kg * 1000

total_food = 0

input_line = input()
while input_line != "Adopted":
    food_gram = int(input_line)

    total_food += food_gram

    input_line = input()

diff_sum = abs(food_gr - total_food)

if total_food <= food_gr:
    print(f"Food is enough! Leftovers: {diff_sum} grams." )
elif total_food > food_gr:
    print(f"Food is not enough. You need {diff_sum} grams more." )