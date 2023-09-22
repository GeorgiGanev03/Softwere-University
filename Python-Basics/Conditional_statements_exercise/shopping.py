budget = float(input())
video_cards = int(input())
procesors = int(input())
ram = int(input())

video_card_price = video_cards * 250
procesor_price = procesors * (video_card_price * 0.35)
ram_price = ram * (video_card_price * 0.10)

final_sum = video_card_price + procesor_price + ram_price

if video_cards > procesors:
    discount = final_sum - (final_sum * 0.15)
    #final_sum = final_sum * 0.85

#final_price = abs(budget - final_sum)
final_price = abs(budget - discount)

if discount <= budget:
    print(f"You have {final_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {final_price:.2f} leva more!")

