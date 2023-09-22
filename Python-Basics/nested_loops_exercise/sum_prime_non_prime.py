prime_number = 0
non_prime_number = 0

input_line = input()
while input_line != "stop":
    current_number = int(input_line)

    if current_number < 0:
        print(f"Number is negative.")
        input_line = input()
        continue

    count = 0
    for j in range(1, current_number + 1):
        if current_number % j == 0:
              count += 1

    if count == 2:
        prime_number += current_number
    else:
        non_prime_number += current_number

    input_line = input()

print(f"Sum of all prime numbers is: {prime_number}")
print(f"Sum of all non prime numbers is: {non_prime_number}")
