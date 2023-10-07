def odd_and_even(number):
    even_sum = 0
    odd_sum = 0
    for letter in number:
        if int(letter) % 2 == 0:
            even_sum += int(letter)
        else:
            odd_sum += int(letter)
    return odd_sum, even_sum


number = input()

sum_of_odd, sum_of_even = odd_and_even(number)

print(f"Odd sum = {sum_of_odd}, Even sum = {sum_of_even}")



