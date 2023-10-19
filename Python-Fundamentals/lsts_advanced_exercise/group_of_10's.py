numbers = [int(number) for number in input().split(", ")]
group_of_number = 10

while numbers:
    filtered_number = [number for number in numbers if number <= group_of_number]
    print(f"Group of {group_of_number}'s: {filtered_number}")
    group_of_number += 10
    numbers = [number for number in numbers if number not in filtered_number]


