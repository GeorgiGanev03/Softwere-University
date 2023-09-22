team = input()
souvenirs = input()
bought_souvenirs = int(input())

price = 0

if team == "Argentina":
    if souvenirs == "flags":
        price = 3.25
    elif souvenirs == "caps":
        price = 7.20
    elif souvenirs == "posters":
        price = 5.10
    elif souvenirs == "stickers":
        price = 1.25
    else:
        print(f"Invalid stock!")
elif team == "Brazil":
    if souvenirs == "flags":
        price = 4.20
    elif souvenirs == "caps":
        price = 8.50
    elif souvenirs == "posters":
        price = 5.35
    elif souvenirs == "stickers":
        price = 1.20
    else:
        print(f"Invalid stock!")
elif team == "Croatia":
    if souvenirs == "flags":
        price = 2.75
    elif souvenirs == "caps":
        price = 6.90
    elif souvenirs == "posters":
        price = 4.95
    elif souvenirs == "stickers":
        price = 1.10
    else:
        print(f"Invalid stock!")
elif team == "Denmark":
    if souvenirs == "flags":
        price = 3.10
    elif souvenirs == "caps":
        price = 6.50
    elif souvenirs == "posters":
        price = 4.80
    elif souvenirs == "stickers":
        price = 0.90
    else:
        print(f"Invalid stock!")
else:
    print(f"Invalid country!")

total_sum = price * bought_souvenirs

if team == "Argentina" or team == "Brazil" or team == "Croatia" or team == "Denmark":
    if souvenirs == "flags" or souvenirs == "caps" or souvenirs == "posters" or souvenirs == "stickers":
        print(f"Pepi bought {bought_souvenirs} {souvenirs} of {team} for {total_sum:.2f} lv.")
    