import sys

number = -sys.maxsize

while True:
    current_number = input()

    if current_number == "Stop":
        break

    num = float(current_number)

    if num > number:
        number = num

print(round(number))



