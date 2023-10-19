string_list = [fruit for fruit in input().split() if len(fruit) % 2 == 0]
print(*string_list, sep="\n")