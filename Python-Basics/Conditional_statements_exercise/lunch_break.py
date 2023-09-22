import math

serial = input()
time_of_episode = int(input())
break_rest = int(input())

lunch_break = break_rest * 1/8
rest_time = break_rest * 1/4
time_left = break_rest - lunch_break - rest_time

time = abs(time_left - time_of_episode)

final_time = math.ceil(time)
if time_left >= time_of_episode:
    print(f"You have enough time to watch {serial} and left with {final_time} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial}, you need {final_time} more minutes.")




