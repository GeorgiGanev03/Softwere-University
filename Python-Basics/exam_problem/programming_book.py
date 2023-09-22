price_for_page = float(input())
price_for_cover = float(input())
discount_for_paper = int(input())
price_for_designer = float(input())
percent_total_sum = int(input())

price_for_print = price_for_page * 899 + price_for_cover * 2

discount = discount_for_paper / 100

discount_for_print = price_for_print * discount

price_discount = price_for_print - discount_for_print

paying_for_designer = price_discount + price_for_designer

discount_total_sum = percent_total_sum / 100

discount_sum = paying_for_designer * discount_total_sum

total_sum = paying_for_designer - discount_sum

print(f"Avtonom should pay {total_sum:.2f} BGN.")





