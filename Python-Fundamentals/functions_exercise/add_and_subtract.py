def sum_numbers(num_1, num_2):
    return num_1 + num_2

def subtract(result, num_3):
    return result - num_3

def add_and_subtract(num_1, num_2, num_3):
    sum = sum_numbers(num_1, num_2)
    subtract_num = subtract(sum, num_3)
    return subtract_num


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

result = add_and_subtract(num_1, num_2, num_3)

print(result)
