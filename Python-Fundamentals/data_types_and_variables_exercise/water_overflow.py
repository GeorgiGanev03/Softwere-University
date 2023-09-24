n = int(input())

water_tank = 255

counter = 0

for liters in range(n):
    liters_of_water = int(input())

    water_tank -= liters_of_water

    if water_tank < 0:
        print(f"Insufficient capacity!")
        water_tank += liters_of_water
        continue

    counter += liters_of_water

print(counter)
