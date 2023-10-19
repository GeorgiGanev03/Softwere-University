words = input().split()

new_list = []
index = 0
for word in words:
    number = ""
    ascii_letter = ""
    bool_flag = False
    current_word = []
    for letter in word:
        if letter.isdigit():
            number += letter
            continue
        if bool_flag == False:
            ascii_letter = chr(int(number))
            new_list.append(ascii_letter)
            bool_flag = True
        new_list[index] += letter
    current_word.append(new_list[index])
    current_word_list = list(current_word[0])
    current_word_list[1], current_word_list[-1] = current_word_list[-1], current_word_list[1]
    new_word = "".join(current_word_list)
    new_list.pop(index)
    new_list.append(new_word)
    index += 1
    if bool_flag:
        bool_flag = False

print(" ".join(new_list))