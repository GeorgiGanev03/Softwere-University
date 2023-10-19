def to_do_notes():
    note_list = []

    while True:
        command = input()

        if command == "End":
            break

        note_list.append(command)

    sorted_notes = sorted(note_list, key=lambda note: int(note.split("-")[0]))

    return [note.split("-")[1] for note in sorted_notes]


result = to_do_notes()

print(result)
