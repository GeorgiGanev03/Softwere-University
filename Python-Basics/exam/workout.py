import math

days = int(input())
kilometers = float(input())

first_num = kilometers
first_day = kilometers

total_kilometers = 0

for day in range(1, days + 1):
    day_kilometers = int(input())

    percent = day_kilometers / 100

    percent_km = first_day * percent

    first_day += percent_km

    total_kilometers += first_day

total_kilometers += first_num

diff_sum = abs(1000 - total_kilometers)

if total_kilometers >= 1000:
    print(f"You've done a great job running {math.ceil(diff_sum)} more kilometers!")
elif total_kilometers < 1000:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(diff_sum)} more kilometers")