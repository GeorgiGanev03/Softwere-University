single_string = input()

filtered_list = []
counter = -1

for letter in single_string:
    counter += 1
    if letter.isupper():
        filtered_list.append(counter)

print(filtered_list)