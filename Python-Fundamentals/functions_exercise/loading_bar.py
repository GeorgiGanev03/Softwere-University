def loading_bar(number):
    percent_list = []
    if number == 100:
        percent_list.append(f"100% Complete!")
        percent_list.append(f"[%%%%%%%%%%]")
    elif number >=1 or number <= 99:
        percent_list.append(f"{number}% [{'%' * (number // 10)}{'.' * (10 - (number // 10))}]")
        percent_list.append(f"Still loading...")

    return percent_list


number = int(input())

percent = loading_bar(number)
print(*percent, sep="\n")



