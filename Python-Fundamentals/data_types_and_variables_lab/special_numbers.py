n = int(input())

for number in range(1, n + 1):
    number_as_string = str(number)

    total_sum = 0

    for digit in number_as_string:
        total_sum += int(digit)

    if total_sum == 5 or total_sum == 7 or total_sum == 11:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")





