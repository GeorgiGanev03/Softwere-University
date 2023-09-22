chiken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

chiken_menu_price = chiken_menu * 10.35
fish_menu_price = fish_menu * 12.40
vegetarian_menu_price = vegetarian_menu * 8.15

total_price = chiken_menu_price + fish_menu_price + vegetarian_menu_price

price = total_price * 0.20

total_sum = total_price + price + 2.50



print(total_sum)