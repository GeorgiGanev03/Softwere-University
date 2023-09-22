num1 = int(input())
num2 = int(input())

for number in range(num2, num1, -1):

    if number % num1 == 0:
        print(number)
        break


