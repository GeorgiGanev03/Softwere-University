
total_tickets = 0
student_ticket = 0
standard_ticket = 0
kid_ticket = 0

movie_name = input()
while movie_name != "Finish":
    total_seats = int(input())

    tickets_movie = 0

    ticket = input()
    while ticket != "End":

        if ticket == "End":
            break

        total_tickets += 1
        tickets_movie += 1

        if ticket == "student":
            student_ticket += 1
        elif ticket == "standard":
            standard_ticket += 1
        else:
            kid_ticket += 1

        if tickets_movie == total_seats:
            break

        ticket = input()

    percent_sold_tickets = tickets_movie / total_seats * 100

    print(f"{movie_name} - {percent_sold_tickets:.2f}% full.")

    movie_name = input()

percent_student = student_ticket / total_tickets * 100
percent_standard = standard_ticket / total_tickets * 100
percent_kid = kid_ticket / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kid:.2f}% kids tickets.")