city = input()
sells = float(input())
commision = 0

wrong_data = False

if city == "Sofia":
    if 0 <= sells <= 500:
        commision = sells * 0.05
    elif 500 <= sells <= 1000:
        commision = sells * 0.07
    elif 1000 <= sells <= 10000:
        commision = sells * 0.08
    elif sells > 10000:
        commision = sells * 0.12
    else:
        wrong_data = True

elif city == "Varna":
    if 0 <= sells <= 500:
        commision = sells * 0.045
    elif 500 <= sells <= 1000:
        commision = sells * 0.075
    elif 1000 <= sells <= 10000:
        commision = sells * 0.10
    elif sells > 10000:
        commision = sells * 0.13
    else:
        wrong_data = True

elif city == "Plovdiv":
    if 0 <= sells <= 500:
        commision = sells * 0.055
    elif 500 <= sells <= 1000:
        commision = sells * 0.08
    elif 1000 <= sells <= 10000:
        commision = sells * 0.12
    elif sells > 10000:
        commision = sells * 0.145
    else:
        wrong_data = True

else:
    wrong_data = True

if wrong_data:
    print("error")
else:
    print(f"{commision:.2f}")






