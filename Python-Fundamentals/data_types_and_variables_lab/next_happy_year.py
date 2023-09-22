year = int(input())

bool_flag = False

while not bool_flag:
    year += 1

    year_as_string = str(year)

    bool_flag = True

    for digit in year_as_string:
        if year_as_string.count(digit) > 1:
            bool_flag = False
            break

print(year)


