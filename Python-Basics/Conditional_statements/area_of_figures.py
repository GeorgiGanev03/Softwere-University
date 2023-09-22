import math

figure = input()
area = 0

if figure == "square":
    num1 = float(input())
    area = num1 * num1

elif figure == "rectangle":
    num1 = float(input())
    num2 = float(input())
    area = num1 * num2

elif figure == "circle":
    r = float(input())
    area = math.pi * (r ** 2)

elif figure == "triangle":
    num1 = float(input())
    num2 = float(input())
    area = 1 / 2 * num1 * num2

print(f'{area:.3f}')