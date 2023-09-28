n = int(input())

positives = []
negatives = []

for number in range(n):
    numbers = int(input())

    if numbers >= 0:
        positives.append(numbers)

    elif numbers < 0:
        negatives.append(numbers)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")

