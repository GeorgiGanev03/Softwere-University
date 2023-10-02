string_of_integers = input().split(", ")
beggars = int(input())

numbers_list = []

for current_money in string_of_integers:
    numbers_list.append(int(current_money))

total_sum = []

for beggar in range(0, beggars):
    total_sums = 0
    current_index = 0
    for index in range(beggar, len(numbers_list), beggars):
        total_sums += numbers_list[index]

    total_sum.append(total_sums)

print(total_sum)
