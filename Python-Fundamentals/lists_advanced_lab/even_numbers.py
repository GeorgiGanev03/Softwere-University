numbers_list = list(map(int, input().split(", ")))

found_even_numbers = map(lambda number: number if numbers_list[number] % 2 == 0 else 'no', range(len(numbers_list)))

even_numbers = list(filter(lambda x: x != 'no', found_even_numbers))
print(even_numbers)




