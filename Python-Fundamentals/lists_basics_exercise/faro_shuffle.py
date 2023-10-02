string_input = input().split()
count_of_shuffles = int(input())

for shuffle in range(count_of_shuffles):
    middle_of_cards = len(string_input) // 2
    first_part = string_input[0:middle_of_cards]
    second_part = string_input[middle_of_cards:]

    after_shuffling = []

    for index in range(len(second_part)):

        after_shuffling.append(first_part[index])
        after_shuffling.append(second_part[index])

    string_input = after_shuffling

print(string_input)

