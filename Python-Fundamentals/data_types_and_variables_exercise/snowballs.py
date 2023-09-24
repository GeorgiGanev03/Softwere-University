n = int(input())

current_value = 0
weight = 0
time = 0
quality = 0

for snowball in range(1, n + 1):

    weight_of_snowball = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    value = (weight_of_snowball / snowball_time) ** snowball_quality

    if value > current_value:
        current_value = value
        weight = weight_of_snowball
        time = snowball_time
        quality = snowball_quality

print(f"{weight} : {time} = {int(current_value)} ({quality})")






