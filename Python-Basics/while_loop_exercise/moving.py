width = int(input())
lenght = int(input())
hight = int(input())

available_meters = width * lenght * hight
meter_counter = 0

input_line = input()
while input_line != "Done":
    boxes = int(input_line)

    meter_counter += boxes

    diff_sum = available_meters - meter_counter

    if diff_sum < 0:
        break

    input_line = input()

diff_sum = abs(available_meters - meter_counter)
if input_line == "Done":
    print(f"{diff_sum} Cubic meters left.")
else:
    print(f"No more free space! You need {diff_sum} Cubic meters more.")

