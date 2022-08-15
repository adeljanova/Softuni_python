book = input()
books_checked = 0
new_book = input()
while new_book != "No More Books":
    if new_book == book:
        print(f"You checked {books_checked} books and found it.")
        break
    books_checked += 1
    new_book = input()
if new_book == "No More Books":
    print(f"The book you search is not here!")
    print(f"You checked {books_checked} books.")





