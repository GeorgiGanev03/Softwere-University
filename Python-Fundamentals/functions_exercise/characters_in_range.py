def ascii(char_1, char_2):
    char_list = []
    for letter in range(ord(char_1) + 1, ord(char_2)):
        char_list.append(chr(letter))
    return char_list


input_1 = input()
input_2 = input()

result = ascii(input_1, input_2)

print(*result, sep=" ")