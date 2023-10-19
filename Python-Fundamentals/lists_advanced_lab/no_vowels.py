example_string = input()

sorted_text = [letter for letter in example_string if letter.lower() not in ['a', 'o', 'u', 'e', 'i']]

print(*sorted_text, sep="")





