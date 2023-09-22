worst_grades = int(input())

sum_grade = 0
grade_count = 0

last_name = ""

poor_grades = 0

flag = False

problem_name = input()
while problem_name != "Enough":
    grade = float(input())

    sum_grade += grade
    grade_count += 1


    last_name = problem_name

    if grade <= 4:
        poor_grades += 1

    if poor_grades >= worst_grades:
        flag = True
        break

    problem_name = input()

if flag:
    print(f"You need a break, {poor_grades} poor grades.")
else:
    average_grade = sum_grade / grade_count
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {grade_count}")
    print(f"Last problem: {last_name}")





