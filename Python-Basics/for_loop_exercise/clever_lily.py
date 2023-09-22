age_of_lily = int(input())
washingmachine_price = float(input())
price_toy = int(input())

birthday_money = 0
toy_count = 0
stolen_money = 0

for year in range(1, age_of_lily+1):
    if year % 2 == 0:
        birthday_money += int(year / 2) * 10
        stolen_money += 1
    else:
        toy_count += 1

sold_toys = toy_count * price_toy

total_money = birthday_money + sold_toys - stolen_money

diff_price = abs(total_money - washingmachine_price)

if total_money >= washingmachine_price:
    print(f"Yes! {diff_price:.2f}")
else:
    print(f"No! {diff_price:.2f}")



