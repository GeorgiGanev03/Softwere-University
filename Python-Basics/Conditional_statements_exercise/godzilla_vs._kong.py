budget = float(input())
count_of_items = int(input())
price_outfit = float(input())

price_decor = budget * 0.10
sum_outfit = count_of_items * price_outfit

if count_of_items > 150:
    sum_outfit = sum_outfit * 0.90

end_price = price_decor + sum_outfit

final_budget = abs(budget - end_price)

if budget >= end_price:
    print("Action!")
    print(f"Wingard starts filming with {final_budget:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {final_budget:.2f} leva more.")