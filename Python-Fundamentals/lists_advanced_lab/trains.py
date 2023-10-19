wagons = int(input())
train = [0] * wagons

while True:
    command = input().split()

    if command[0] == "End":
        break

    if command[0] == "add":
        number_of_people = int(command[1])
        train[-1] += number_of_people

    if command[0] == "insert":
        index = int(command[1])
        number_of_people = int(command[2])
        train[index] += number_of_people

    if command[0] == "leave":
        index = int(command[1])
        number_of_people = int(command[2])
        train[index] -= number_of_people

print(train)