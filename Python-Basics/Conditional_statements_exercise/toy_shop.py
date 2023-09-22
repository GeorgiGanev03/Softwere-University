vacantion_price = float(input())
puzzle = int(input())
dolls = int(input())
teddy_bear = int(input())
minion = int(input())
trucks = int(input())
discount = 0

total_sum = puzzle * 2.60 + dolls * 3 + teddy_bear * 4.10 + minion * 8.20 + trucks * 2

count_toy = puzzle + dolls + teddy_bear + minion + trucks

if count_toy >= 50:
    discount = total_sum * 0.25

final_price = total_sum - discount

rent = final_price * 0.10

profit = final_price - rent

money_for_vacantion = abs(profit - vacantion_price)

if money_for_vacantion >= vacantion_price:
    print(f"Yes! {money_for_vacantion:.2f} lv left.")
elif money_for_vacantion <= vacantion_price:
    print(f"Not enough money! {money_for_vacantion:.2f} lv needed.")

