first_word = input()
second_word = input()

counter = 0

old_string = first_word

for letter1 in range(len(first_word)):
    first_part = ""
    second_part = ""

    new_string = ""

    first_part += second_word[0:letter1 + 1]
    second_part += first_word[letter1 + 1:]

    new_string += first_part + second_part

    if new_string == old_string:
        continue

    print(new_string)

    old_string = new_string




