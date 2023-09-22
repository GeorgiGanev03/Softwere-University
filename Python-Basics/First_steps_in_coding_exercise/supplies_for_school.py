num_of_pen = int(input())
num_of_marker = int(input())
board_preparation = int(input())
percent_off = int(input())

price_of_pen = num_of_pen * 5.80
price_of_marker = num_of_marker * 7.20
price_of_preparation = board_preparation * 1.20
price_for_everything = price_of_pen + price_of_marker + price_of_preparation

price_with_percent_off = price_for_everything - (price_for_everything * percent_off / 100)

print(price_with_percent_off)       