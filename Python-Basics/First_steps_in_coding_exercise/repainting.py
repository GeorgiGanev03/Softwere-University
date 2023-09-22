nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

price_for_nylon = (nylon + 2) * 1.50
price_for_paint = (paint * 1.1) * 14.50
price_for_thinner = (thinner * 5)
price_for_bags = 0.40

price_for_everything = price_for_nylon + price_for_paint + price_for_thinner + price_for_bags

price = hours * (price_for_everything * 0.30)

total = price_for_everything + price

print(total)