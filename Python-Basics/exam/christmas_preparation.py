wrapping_paper = int(input())
clothes = int(input())
glue = float(input())
percent_discount = int(input())

price_wrapping_paper = 5.80
price_clothes = 7.20
price_glue = 1.20

sum_wrapping_paper = wrapping_paper * price_wrapping_paper
sum_clothes = clothes * price_clothes
sum_glue = glue * price_glue

total_sum = sum_wrapping_paper + sum_clothes + sum_glue

discount = percent_discount / 100

total_price = total_sum - total_sum * discount

print(f"{total_price:.3f}")