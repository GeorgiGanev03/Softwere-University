numbers_as_string = input().split()

new_list = []

for number in numbers_as_string:
    new_list.append(abs(float(number)))

print(new_list, sep=" ")


