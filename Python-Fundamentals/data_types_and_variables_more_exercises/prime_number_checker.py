n = int(input())
counter = 0
for digit in range(1, n + 1):

    if n % digit == 0:
        counter += 1

if counter == 2:
    print(f"True")
else:
    print(f"False")