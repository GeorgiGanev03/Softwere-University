def is_palindrome(string_of_numbers: str) -> bool:
    return string_of_numbers == string_of_numbers[::-1]


number_as_string = input().split(", ")

for number_as_string in number_as_string:
    print(is_palindrome(number_as_string))

#numbers_as_string = input().split(", ")
#
#numbers_list = []
#reversed_list = []
#for number in numbers_as_string:
#    numbers_list.append(number)
#for number in numbers_list:
#    reversed_list.append(number[::-1])
#
#for i in range(0, len(numbers_list)):
#    if numbers_list[i] == reversed_list[i]:
#        print("True")
#    else:
#        print("False")





