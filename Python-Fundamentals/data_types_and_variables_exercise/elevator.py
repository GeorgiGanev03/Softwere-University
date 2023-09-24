persons = int(input())
capacity = int(input())

total_sum = persons

counter = 0

while total_sum > 0:
        counter += 1
        total_sum -= capacity
print(counter)