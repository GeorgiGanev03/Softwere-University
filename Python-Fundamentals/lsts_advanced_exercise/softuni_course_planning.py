def add(lesson_title):
    if lesson_title in lessons:
        pass
    else:
        lessons.append(lesson_title)


def insert(lesson_title, index):
    lesson_title = command[1]
    index = int(command[2])

    if lesson_title in lessons:
        pass
    else:
        lessons.insert(index, lesson_title)


def remove(lesson_title):
    if lesson_title in lessons:
        lessons.remove(lesson_title)
    else:
        pass


def check_for_exercise(find_index):
    if len(lessons) - 1 > find_index:
         if "Exercise" in lessons[find_index + 1]:
             return True
    return False


def swap(lesson_title_1, lesson_title_2):
    if lesson_title_1 in lessons and lesson_title_2 in lessons:
        lesson_1, lesson_2 = lessons.index(lesson_title_1), lessons.index(lesson_title_2)
        lessons[lesson_1], lessons[lesson_2] = lessons[lesson_2], lessons[lesson_1]
        if check_for_exercise(lesson_1):
            lessons.insert(lesson_2 + 1, lessons.pop(lesson_1 + 1))
        if check_for_exercise(lesson_2):
            lessons.insert(lesson_1 + 1, lessons.pop(lesson_2 + 1))


def exercise(lesson_title):
    if lesson_title in lessons:
        lesson_index = lessons.index(lesson_title)
        if not check_for_exercise(lesson_index):
            lessons.insert(lesson_index + 1, f"{lesson_title}-Exercise")
        #result = f"{lesson_title} - Exercise"
        #lesson_index = lessons.index(lesson_title)
        #lessons.remove(lesson_title)
        #lessons.insert(lesson_index, result)
    elif lesson_title not in lessons:
        lessons.append(lesson_title)
        lessons.append(f"{lesson_title}-Exercise")


lessons = [lesson for lesson in input().split(", ")]

command = input().split(":")
while command[0] != "course start":
    if command[0] == "Add":
        lesson_type = [command[1]]
        add("".join(lesson_type))

    elif command[0] == "Insert":
        lesson_title = command[1]
        index = int(command[2])
        insert("".join(lesson_title), index)

    elif command[0] == "Remove":
        lesson_title = command[1]
        remove(lesson_title)

    elif command[0] == "Swap":
        lesson_title_1 = command[1]
        lesson_title_2 = command[2]
        swap(lesson_title_1, lesson_title_2)

    elif command[0] == "Exercise":
        lesson_title = command[1]
        exercise(lesson_title)


    command = input().split(":")


for number, lesson in enumerate(lessons):
    print(f"{number + 1}.{''.join(lesson)}")