number_of_cats = int(input())

total_food = 0

group_1 = 0
group_2 = 0
group_3 = 0

for gr in range(1, number_of_cats + 1):

    food_gr = float(input())
    total_food += food_gr

    if 100 <= food_gr <= 199:
        group_1 += 1
    elif 200 <= food_gr <= 299:
        group_2 += 1
    elif 300 <= food_gr <= 400:
        group_3 += 1

price_food = total_food / 1000

total_sum = price_food * 12.45

print(f"Group 1: {group_1} cats.")
print(f"Group 2: {group_2} cats.")
print(f"Group 3: {group_3} cats.")
print(f"Price for food per day: {total_sum:.2f} lv.")
