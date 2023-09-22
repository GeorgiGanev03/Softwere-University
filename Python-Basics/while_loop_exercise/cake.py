width = int(input())
length = int(input())

cake = width * length

total_sum = 0

input_line = input()
while input_line != "STOP":
    pieces = int(input_line)

    cake -= pieces
    total_sum += pieces

    if cake <= 0:
        break

    input_line = input()

diff_sum = abs(cake)
if input_line == "STOP":
    print(f"{diff_sum} pieces are left.")
else:
    print(f"No more cake left! You need {diff_sum} pieces more.")


