hour_exam = int(input())
min_exam = int(input())
hour_arrival = int(input())
min_arrival = int(input())

exam_all_min = (hour_exam * 60) + min_exam
arrival_all_min = (hour_arrival * 60) + min_arrival
minutes = abs(arrival_all_min - exam_all_min)

if arrival_all_min > exam_all_min:
    print("Late")
    if minutes >= 60:
        hour = minutes // 60
        mins = minutes % 60
        print(f"{hour}:{mins:02d} hours after the start")
    else:
        print(f"{minutes} minutes after the start")
elif arrival_all_min == exam_all_min or minutes <= 30:
    print("On time")
    if minutes > 0:
        print(f"{minutes} minutes before the start")
else:
    print("Early")
    if minutes >= 60:
        hour = minutes // 60
        mins = minutes % 60
        print(f"{hour}:{mins:02d} hours before the start")
    else:
        print(f"{minutes} minutes before the start")