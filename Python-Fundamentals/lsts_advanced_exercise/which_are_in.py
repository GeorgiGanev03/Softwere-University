current_strings = input().split(", ")
substrings = input().split(", ")
strings_list = []
substrings_list = []
for string in current_strings:
    for substring in substrings:
        if string in substring:
            substrings_list.append(string)
            break

print(substrings_list)