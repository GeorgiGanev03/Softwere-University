budget = int(input())

total_sum = 0

input_line = input()
while input_line != "End":

    prices = int(input_line)

    total_sum += prices

    if total_sum > budget:
        print(f"You went in overdraft!")
        break


    input_line = input()

else:
    print(f"You bought everything needed.")