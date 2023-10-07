def factorial(number):
    for multiplier in range(1, number):
        number *= multiplier

    return number


num_1 = int(input())
num_2 = int(input())

first_value = factorial(num_1)
second_value = factorial(num_2)
result = first_value / second_value

print(f"{result:.2f}")




