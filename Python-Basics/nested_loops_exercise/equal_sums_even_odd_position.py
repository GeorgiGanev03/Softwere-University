first_num = int(input())
second_num = int(input())

for n in range(first_num, second_num + 1):
    current_num = str(n)

    even_sum = 0
    odd_sum = 0
    for j in range(0, len(current_num)):
        digits = int(current_num[j])

        if j % 2 == 0:
            even_sum += digits
        else:
            odd_sum += digits

    if even_sum == odd_sum:
        print(n, end=" ")

