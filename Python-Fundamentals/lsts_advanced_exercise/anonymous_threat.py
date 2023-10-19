strings = input().split()

strings_list = list(strings)

command = input().split()
while command[0] != "3:1":
    if command[0] == "merge":
        current_command = command[0]
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if end_index > len(strings) - 1:
            end_index = len(strings) - 1
        merged_string = "".join(strings[start_index:end_index + 1])
        strings[start_index:end_index + 1] = [merged_string]

    elif command[0] == "divide":
        current_command = command[0]
        index = int(command[1])
        partitions = int(command[2])
        element = strings[index]
        element_part = []
        partition_len = len(element) // partitions

        for current_element in range(partitions):
            if current_element != partitions - 1:
                element_part.append(element[current_element * partition_len: (current_element + 1) * partition_len])
            else:
                element_part.append(element[current_element * partition_len:])

        strings.pop(index)
        for i in range(len(element_part)):
            strings.insert(index + i, element_part[i])
    command = input().split()

print(" ".join(strings))
