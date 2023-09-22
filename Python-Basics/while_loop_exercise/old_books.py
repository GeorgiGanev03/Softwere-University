book_name = input()

book_count = 0

while True:
    current_book = input()

    if book_name == current_book:
        print(f"You checked {book_count} books and found it.")
        break


    elif current_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {book_count} books.")
        break

    book_count += 1

