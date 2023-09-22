number = int(input())

left_sum = 0
right_sum = 0

for n in range(number*2):
    current_number = int(input())

    if n < number:
        left_sum += current_number
    elif n >= number:
        right_sum += current_number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff_numbers = abs(left_sum - right_sum)
    print(f"No, diff = {diff_numbers}")

