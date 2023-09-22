first_interval = int(input())
final_interval = int(input())
magic_num = int(input())

combination_count = 0

flag = False

for x in range(first_interval, final_interval+1):
    for y in range(first_interval, final_interval + 1):

        combination_count += 1

        if x + y == magic_num:
            flag = True
            print(f"Combination N:{combination_count} ({x} + {y} = {magic_num})")
            break

    if flag:
        break

else:
    print(f"{combination_count} combinations - neither equals {magic_num}")



