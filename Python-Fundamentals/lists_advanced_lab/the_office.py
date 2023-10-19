numbers_list = list(map(int, input().split()))
factor = int(input())

average = 0

numbers = list(map(lambda x: x * factor, numbers_list))

for number in numbers:
    average += number

average_sum = average // len(numbers)

filtered_list = []

counter = 0
for number in numbers:
    if number > average_sum:
        filtered_list.append(number)
        counter += 1

if counter >= len(numbers) // 2:
    print(f"Score: {counter}/{len(numbers)}. Employees are happy!")
else:
    print(f"Score: {counter}/{len(numbers)}. Employees are not happy!")