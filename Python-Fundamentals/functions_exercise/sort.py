numbers_as_string = input().split()

new_list = []
for digit in numbers_as_string:
    new_list.append(int(digit))

new_list.sort()

print(new_list)

