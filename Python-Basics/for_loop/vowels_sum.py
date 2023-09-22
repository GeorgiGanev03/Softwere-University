text = input()

point = 0

for letter in text:
    if letter == "a":
        point += 1
    elif letter == "e":
        point += 2
    elif letter == "i":
        point += 3
    elif letter == "o":
        point += 4
    elif letter == "u":
        point += 5

print(point)


