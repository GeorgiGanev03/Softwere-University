n = int(input())

for number in range(1, n + 1):
    num = int(input())

    if num % 2 == 1:
        print(f"{num} is odd!")
        break

    if num % 2 == 0:
        continue

else:
    print("All numbers are even.")





