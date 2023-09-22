hour = int(input())
minutes = int(input())

time = (hour * 60) + minutes + 15

hours = time // 60
minute = time % 60

if hours > 23:
    hours = 0
print(f"{hours}:{minute:02}")