most_powerful_word = ""
most_powerful_word_ascii = 0

while True:
    word = input()

    if word == "End of words":
        break

    current_word = 0

    for letter in word:
        current_word += ord(letter)

    if word[0].lower() in "aeiouy":
        current_word = current_word * len(word)
    else:
        current_word = current_word // len(word)

    if current_word > most_powerful_word_ascii:
        most_powerful_word_ascii = current_word
        most_powerful_word = word

print(f"The most powerful word is {most_powerful_word} - {most_powerful_word_ascii}" )




