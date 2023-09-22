heritage = float(input())
last_year = int(input())

age = 18

for year in range(1800, last_year+1):

    if year % 2 == 0:
        heritage -= 12000
    else:
        heritage -= (12000 + 50 * age)
    age += 1

diff_sum = abs(heritage)

if heritage >= diff_sum:
    print(f"Yes! He will live a carefree life and will have {diff_sum:.2f} dollars left.")
elif heritage <= diff_sum:
    print(f"He will need {diff_sum:.2f} dollars to survive.")
