number_of_loads = int(input())

microbus = 0
truck = 0
train = 0

sum_of_tons = 0

for sold_load in range(0, number_of_loads):
    tons_of_load = int(input())

    if tons_of_load <= 3:
        microbus += tons_of_load
        sum_of_tons += tons_of_load
    elif 4 <= tons_of_load < 11:
        truck += tons_of_load
        sum_of_tons += tons_of_load
    elif tons_of_load >= 11:
        train += tons_of_load
        sum_of_tons += tons_of_load

total_sum = microbus + truck + train

print(f"{(microbus * 200 + truck * 175 + train * 120) / sum_of_tons:.2f}")
print(f"{(microbus / sum_of_tons) * 100:.2f}%")
print(f"{(truck / sum_of_tons) * 100:.2f}%")
print(f"{(train / sum_of_tons) * 100:.2f}%")