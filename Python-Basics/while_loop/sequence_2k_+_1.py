number = int(input())

counter = 1

while True:
    print(counter)

    counter = 2 * counter + 1

    if counter > number:
        break