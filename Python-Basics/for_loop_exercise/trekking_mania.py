group_number = int(input())

total_sum = 0

musala, monblan, kilimanjaro, k2, everest, = 0, 0, 0, 0, 0,

for n in range(1, group_number+1):
    current_number = int(input())

    total_sum += current_number

    if current_number <= 5:
        musala += current_number
    elif 6 <= current_number <= 12:
        monblan += current_number
    elif 13 <= current_number <= 25:
        kilimanjaro += current_number
    elif 26 <= current_number <= 40:
        k2 += current_number
    elif current_number >= 41:
        everest += current_number

musala = musala / total_sum * 100
monblan = monblan / total_sum * 100
kilimanjaro = kilimanjaro / total_sum * 100
k2 = k2 / total_sum * 100
everest = everest / total_sum * 100

print(f"{musala:.2f}%")
print(f"{monblan:.2f}%")
print(f"{kilimanjaro:.2f}%")
print(f"{k2:.2f}%")
print(f"{everest:.2f}%")