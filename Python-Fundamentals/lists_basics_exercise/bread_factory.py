day_events = input().split("|")

energy = 100
coins = 100

day_over = False

for event in day_events:
    event_info = event.split("-")
    current_event = event_info[0]
    current_number = int(event_info[1])

    current_energy = 0

    if day_over:
        day_over = False

    if current_event == "rest":
        if 100 - energy < current_number:
            current_number = 100 - energy

    #if current_event == "rest":
        #if energy >= 100:
            #energy = 100
            #print(f"You gained 0 energy.")
        #else:
            #energy += current_number
            #print(f"You gained {current_number} energy.")

        #print(f"Current energy: {energy}.")

    elif current_event == "order":
        if energy >= 30:
            energy -= 30
            coins += current_number
            print(f"You earned {current_number} coins.")
        else:
            energy += 50
            print(f"You had to rest!")

    else:
        if coins >= current_number:
            coins -= current_number
            print(f"You bought {current_event}.")
        else:
            print(f"Closed! Cannot afford {current_event}.")
            break

    day_over = True

if day_over:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")



