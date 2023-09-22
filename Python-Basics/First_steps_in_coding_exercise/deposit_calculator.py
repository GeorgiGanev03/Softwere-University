deposit = float(input())
deadline = int(input())
interest = float(input())

maximum_interest = deposit * interest
interest_for_1_month = maximum_interest / 12
sum = deposit + deadline / 100 * interest_for_1_month

print(sum)

