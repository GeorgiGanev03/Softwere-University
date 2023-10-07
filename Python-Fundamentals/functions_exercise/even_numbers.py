def even_numbers(number_as_string):
    number_list = []
    for digit in number_as_string:
        if int(digit) % 2 == 0:
            number_list.append(int(digit))
    return number_list


number_as_string = input().split()
result = even_numbers(number_as_string)
print(result)