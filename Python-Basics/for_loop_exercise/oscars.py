name_actor = input()
points_from_academy = float(input())
judges = int(input())


for n in range(1, judges+1):
    actor = len(input())
    points = float(input())

    total_points = 0
    lenght_name = 0

    total_points += points
    lenght_name += actor

    points_from_academy = points_from_academy + ((lenght_name * points)/2)

    diff_points = abs(1250.5 - points_from_academy)

    if points_from_academy >= 1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {points_from_academy:.1f}!")
        break
else:
    print(f"Sorry, {name_actor} you need {diff_points:.1f} more!")




