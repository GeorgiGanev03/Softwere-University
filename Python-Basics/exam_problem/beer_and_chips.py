import math

name = input()
budget = float(input())
beer = int(input())
chips = int(input())

price_beer = 1.20 * beer

percent_chips = price_beer * 0.45

price_chips = percent_chips * chips

total_sum = price_beer + math.ceil(price_chips)

diff_sum = abs(budget - total_sum)

if total_sum <= budget:
    print(f"{name} bought a snack and has {diff_sum:.2f} leva left.")
else:
    print(f"{name} needs {diff_sum:.2f} more leva!")







