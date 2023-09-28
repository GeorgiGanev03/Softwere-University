n = int(input())
string_input = input()

normal_list = []
filtered_list = []

for string in range(n):
    strings = input()

    normal_list.append(strings)

    if string_input in strings:
        filtered_list.append(strings)

print(normal_list)
print(filtered_list)



