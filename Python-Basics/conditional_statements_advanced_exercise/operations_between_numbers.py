num_1 = int(input())
num_2 = int(input())
operator = input()

result = 0
flag_bool = False

if operator == "+":
    result = num_1 + num_2
elif operator == "-":
    result = num_1 - num_2
elif operator == "*":
    result = num_1 * num_2
elif operator == "/":
    if num_2 == 0:
        flag_bool = True
    else:
        result = num_1 / num_2
elif operator == "%":
    if num_2 == 0:
        flag_bool = True
    else:
        result = num_1 % num_2

if operator == "+" or operator == "-" or operator == "*":
    if result % 2 == 0:
        print(f"{num_1} {operator} {num_2} = {result} - even")
    else:
        print(f"{num_1} {operator} {num_2} = {result} - odd")

elif operator == "/":
    if flag_bool:
        print(f"Cannot divide {num_2} by zero")
    else:
        print(f"{num_1} {operator} {num_2} = {result:.2f}")

elif operator == "%":
    if flag_bool:
        print(f"Cannot divide {num_2} by zero")
    else:
        print(f"{num_1} {operator} {num_2} = {result}")

