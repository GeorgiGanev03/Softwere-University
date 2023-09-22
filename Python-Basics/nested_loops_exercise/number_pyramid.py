n = int(input())

flag = False
current = 1
for rows in range(1, n+1):
    for cols in range(1, rows+1):
        print(current, end=" ")

        current += 1

        if current > n:
            flag = True
            break

    if flag:
        break

    print()

