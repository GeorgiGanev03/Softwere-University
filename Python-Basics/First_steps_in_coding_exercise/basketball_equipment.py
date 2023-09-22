price_for_year = int(input())

shoes = price_for_year - price_for_year * 0.40
outfit = shoes - shoes * 0.20
basketball = outfit / 4
accessories = basketball / 5

total_price = price_for_year + shoes + outfit + basketball + accessories

print(total_price)
