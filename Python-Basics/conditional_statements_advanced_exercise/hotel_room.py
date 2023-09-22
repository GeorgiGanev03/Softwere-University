month = input()
days = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50 * days
    apartment_price = 65 * days

elif month == "June" or month == "September":
    studio_price = 75.20 * days
    apartment_price = 68.70 * days

elif month == "July" or month == "August":
    studio_price = 76 * days
    apartment_price = 77 * days

if days > 14 and (month == "May" or month == "October"):
    studio_price = studio_price * 0.70
elif days > 7 and (month == "May" or month == "October"):
    studio_price = studio_price * 0.95
elif days > 14 and (month == "June" or month == "September"):
    studio_price = studio_price * 0.80

if days > 14:
    apartment_price = apartment_price * 0.90

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")



