numbers = input().split()

numbers_list = []

for number in numbers:
    numbers_list.append(round(float(number)))

print(numbers_list, sep=" ")


