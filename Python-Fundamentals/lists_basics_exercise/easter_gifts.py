present_strings = input().split()
new_list = []
index = 0

for index in range(0, 1):
    for word in present_strings:
        new_list.append(present_strings[index])
        index += 1
command = input()
while command != "No Money":
    command_type, *other_info = command.split()
    if "OutOfStock" in command_type:
        for number in command:
            type_of_command, type_of_gift = command.split()
            for index in range(len(new_list)):
                if new_list[index] == type_of_gift:
                    new_list[index] = "None"

    elif "Required" in command_type:
        for number in command:
            element_items = command.split()
            type_of_command = element_items[0]
            type_of_gift = element_items[1]
            number_index = int(element_items[2])
            if 0 <= number_index < len(new_list) - 1:
                new_list[number_index] = type_of_gift

    elif "JustInCase" in command_type:
        for number in command:
            type_of_command, type_of_gift = command.split()
            new_list[-1] = type_of_gift
    command = input()

while "None" in new_list:
    new_list.remove("None")

print(*new_list, sep=" ")
