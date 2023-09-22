tabs = int(input())
salary = int(input())

lost_money = 0

for n in range(1, tabs+1):
    website = input()

    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50

    if salary <= 0:
        print(f"You have lost your salary.")
        break

else:
    print(salary)







