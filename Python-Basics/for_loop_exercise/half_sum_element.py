import sys

n = int(input())
max_num = -sys.maxsize
sum_numbers = 0

for _ in range(0, n):
    current_number = int(input())
    sum_numbers += current_number

    if current_number > max_num:
        max_num = current_number

if sum_numbers - max_num == max_num:
    print(f"Yes")
    print(f"Sum = {max_num}")
else:
    diff_numbers = abs(max_num + max_num - sum_numbers)
    print(f"No")
    print(f"Diff = {diff_numbers}")