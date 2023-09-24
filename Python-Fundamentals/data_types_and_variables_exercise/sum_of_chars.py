n = int(input())

total_sum = 0

for letter in range(n):
    char = input()

    total_sum += ord(char)

print(f"The sum equals: {total_sum}")
