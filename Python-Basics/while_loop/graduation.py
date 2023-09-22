name = input()

total_grade = 0
years = 0
failed_years = 0

while True:
    grade = float(input())

    if grade >= 4:
        total_grade += grade
        years += 1

    else:
        failed_years += 1
        failed_year = years + 1
        if failed_years > 1:
            print(f"{name} has been excluded at {failed_year} grade")
            break

    if years == 12:
        average_grade = total_grade / 12
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break


