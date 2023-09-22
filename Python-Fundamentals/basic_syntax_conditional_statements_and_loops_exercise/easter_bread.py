budget = float(input())
price_for_flour = float(input())

price_for_eggs = price_for_flour * 0.75
#price_for_eggs = price_for_flour - percent_eggs

price_for_milk = (price_for_flour * 1.25) / 4
#price_for_milk = price_for_flour + percent_milk

colored_eggs = 0
for number_loaves in range(1, int(budget) + 1):
    if price_for_flour + price_for_eggs + price_for_milk <= budget:
        budget -= (price_for_flour + price_for_eggs + price_for_milk)
        colored_eggs += 3
        if number_loaves % 3 == 0:
            colored_eggs -= (number_loaves - 2)
    else:
        number_loaves -= 1
        print(f"You made {number_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
        break