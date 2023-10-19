def is_palindrome():
    command = input().split()
    palindrome = input()

    new_list = []

    for word in command:
        if word == word[::-1]:
            new_list.append(word)
    counter = 0
    for word in new_list:
        if word == palindrome and word in new_list:
            counter += 1

    return [new_list, counter]


result, found_palindromes = is_palindrome()
print(result)
print(f"Found palindrome {found_palindromes} times")