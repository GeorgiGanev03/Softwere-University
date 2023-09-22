total_sum = 0

input_line = input()
while input_line != "Going home":
    steps = int(input_line)

    total_sum += steps

    if total_sum > 10000:
        break

    input_line = input()

if input_line == "Going home":
    home_steps = int(input())
    total_sum += home_steps

diff_sum = abs(total_sum - 10000)
if total_sum > 10000:
    print("Goal reached! Good job!")
    print(f"{diff_sum} steps over the goal!")
else:
    print(f"{diff_sum} more steps to reach goal.")



