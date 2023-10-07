def calculate(operator, num_1, num_2):
    if operator == "add":
        return num_1 + num_2
    elif operator == "subtract":
        return num_1 - num_2
    elif operator == "multiply":
        return num_1 * num_2
    elif operator == "divide":
        return num_1 // num_2


parameter = input()
a = int(input())
b = int(input())

print(calculate(parameter, a, b))



