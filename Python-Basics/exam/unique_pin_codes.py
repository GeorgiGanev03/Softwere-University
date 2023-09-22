num1 = int(input())
num2 = int(input())
num3 = int(input())

flag = False
counter = 0

for num_1 in range(1, num1 + 1):
    for num_2 in range(1, num2 + 1):
        for num_3 in range(1, num3 + 1):
            counter += 1

            if num_1 % 2 == 0 and num_3 % 2 == 0:
                if num_2 % counter == 0:
                    flag = True
                    break
                if num_2 == 1 or num_2 == 4:
                    break

                print(f"{num_1} {num_2} {num_3}")