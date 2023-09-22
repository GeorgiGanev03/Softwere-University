calculation_period = int(input())

treated_patients = 0
untreated_patients = 0
medics = 7

for day in range(1, calculation_period+1):
    current_patients = int(input())

    if day % 3 == 0 and untreated_patients > treated_patients:
        medics += 1

    if current_patients > medics:
        treated_patients += medics
        untreated_patients += current_patients - medics
    else:
        treated_patients += current_patients

print(treated_patients)
print(untreated_patients)