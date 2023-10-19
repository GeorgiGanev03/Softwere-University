distance_to_pokemon = [int(number) for number in input().split()]

total_sum = 0

current_removed_element = 0

while distance_to_pokemon:
    number = int(input())

    if number < 0:
        current_removed_element = distance_to_pokemon[0]
        distance_to_pokemon[0] = distance_to_pokemon[-1]
        total_sum += current_removed_element
        for element in range(len(distance_to_pokemon)):
            if distance_to_pokemon[element] <= current_removed_element:
                distance_to_pokemon[element] += current_removed_element
            else:
                distance_to_pokemon[element] -= current_removed_element

    elif number > len(distance_to_pokemon) - 1:
        current_removed_element = distance_to_pokemon[-1]
        distance_to_pokemon[-1] = distance_to_pokemon[0]
        total_sum += current_removed_element
        number = len(distance_to_pokemon) - 1
        i = 0
        for element in range(len(distance_to_pokemon)):
            if distance_to_pokemon[element] <= current_removed_element:
                distance_to_pokemon[element] += current_removed_element
                i += 1
            else:
                distance_to_pokemon[element] -= current_removed_element

    elif 0 <= number <= len(distance_to_pokemon):
        current_removed_element = distance_to_pokemon[number]
        distance_to_pokemon.pop(number)

        for element in range(len(distance_to_pokemon)):
            if distance_to_pokemon[element] <= current_removed_element:
                distance_to_pokemon[element] += current_removed_element
            elif distance_to_pokemon[element] > current_removed_element:
                distance_to_pokemon[element] -= current_removed_element

        total_sum += current_removed_element

print(total_sum)










