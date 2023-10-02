collection = input().split("|")
budget = float(input())

maximum_clothes_price = 50
maximum_shoes_price = 35
maximum_accessories_price = 25.50

profit = 0
original_budget = budget
new_budget = 0
for item in collection:
    item_info = item.split("->")
    type_of_item = item_info[0]
    price_of_item = float(item_info[1])
    if type_of_item == "Clothes":
        if price_of_item > maximum_clothes_price:
            continue
        else:
            if budget < price_of_item:
                continue
            else:
                budget -= price_of_item

    elif type_of_item == "Shoes":
        if price_of_item > maximum_shoes_price:
            continue
        else:
            if budget < price_of_item:
                continue
            else:
                budget -= price_of_item

    elif type_of_item == "Accessories":
        if price_of_item > maximum_accessories_price:
            continue
        else:
            if budget < price_of_item:
                continue
            else:
                budget -= price_of_item

    increased_price = price_of_item + price_of_item * 0.4
    print(f"{increased_price:.2f}", end=" ")


    profit += increased_price - price_of_item

new_budget = original_budget + profit

print()
print(f"Profit: {profit:.2f}")
if new_budget >= 150:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")
