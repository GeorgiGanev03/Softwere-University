numbers_as_string = input().split()
n = int(input())

list_of_numbers = []
for index in range(len(numbers_as_string)):
    list_of_numbers.append(int(numbers_as_string[index]))

for number in range(n):
    list_of_numbers.remove(min(list_of_numbers))
#print(", ".join(map(str, list_of_numbers)))
print(*list_of_numbers, sep=", ")