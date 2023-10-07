def is_perfect_number(number):
    counter = 0
    for digit in range(1, number//2):
        if number % digit == 0:
            counter += digit

    if counter == number // 2:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())

perfect_number = is_perfect_number(number)

print(perfect_number)


