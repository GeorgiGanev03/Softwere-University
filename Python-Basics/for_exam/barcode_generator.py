num1 = input()
num2 = input()

f1 = int(num1[0])
f2 = int(num1[1])
f3 = int(num1[2])
f4 = int(num1[3])

s1 = int(num2[0])
s2 = int(num2[1])
s3 = int(num2[2])
s4 = int(num2[3])

for first_num in range(f1, s1 + 1):
    for second_num in range(f2, s2 + 1):
        for third_num in range(f3, s3 + 1):
            for fourth_num in range(f4, s4 + 1):

                if first_num % 2 != 0 and second_num % 2 != 0 and third_num % 2 != 0 and fourth_num % 2 != 0:
                    print(f"{first_num}{second_num}{third_num}{fourth_num}", end=" ")