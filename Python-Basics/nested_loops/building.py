floors = int(input())
rooms = int(input())

for floor in reversed(range(1, floors+1)):
    for room in range(0, rooms):

        if floor % 2 == 0:
            room_type = "O"
        else:
            room_type = "A"

        if floor == floors:
            room_type = "L"

        print(f"{room_type}{floor}{room}", end=" ")

    print()


