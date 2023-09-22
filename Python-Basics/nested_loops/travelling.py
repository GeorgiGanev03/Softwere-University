flag = False

location = ""

input_line = input()
while input_line != "End":
    goal = float(input())

    saved_cash = 0

    while saved_cash <= goal:
        save = float(input())

        saved_cash += save

        if saved_cash >= goal:
            location = input_line
            break

    input_line = input()

    print(f"Going to {location}!")

    if input_line == "End":
        flag = True

    if flag:
        break
