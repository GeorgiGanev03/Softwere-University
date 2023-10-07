numbers_as_string = input().split()

numbers_list = []
min_number = 0
max_number = 0
total_sum = 0
for digit in numbers_as_string:
    numbers_list.append(int(digit))

min_number = min(numbers_list)
max_number = max(numbers_list)
total_sum = sum(numbers_list)

print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {total_sum}")



