assessments = int(input())

total_grade = 0
grade_count = 0

input_line = input()
while input_line != "Finish":
    presentation = input_line

    presentation_grade = 0
    presentation_grade_count = 0

    for grade in range(1, assessments + 1):
        current_grade = float(input())
        presentation_grade += current_grade
        total_grade += current_grade
        grade_count += 1
        presentation_grade_count += 1

    presentation_total_grade = presentation_grade / presentation_grade_count
    final_grade = total_grade / grade_count

    print(f"{presentation} - {presentation_total_grade:.2f}.")

    input_line = input()

    if input_line == "Finish":
        print(f"Student's final assessment is {final_grade:.2f}.")
