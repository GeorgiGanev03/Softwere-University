n = int(input())

numbers = []

for index in range(n):
    input_line = int(input())
    numbers.append(input_line)

COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"

filtered_list = []

command = input()

if command == "even":
    for number in numbers:
        if number % 2 == 0:
            filtered_list.append(number)

elif command == "odd":
    for number in numbers:
        if number % 2 != 0:
            filtered_list.append(number)

elif command == "negative":
    for number in numbers:
        if number < 0:
            filtered_list.append(number)

elif command == "positive":
    for number in numbers:
        if number >= 0:
            filtered_list.append(number)

print(filtered_list)