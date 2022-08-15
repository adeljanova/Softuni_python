shelf_with_books = input().split("&")
line = input()

while line != "Done":
    line = line.split(" | ")
    command = line[0]
    if command == "Add Book":
        book_name = line[1]
        if book_name not in shelf_with_books:
            shelf_with_books.insert(0, book_name)
    elif command == "Take Book":
        book_name = line[1]
        if book_name in shelf_with_books:
            shelf_with_books.remove(book_name)
    elif command == "Swap Books":
        book_one = line[1]
        book_two = line[2]
        if book_one in shelf_with_books and book_two in shelf_with_books:
            index_book_one = shelf_with_books.index(book_one)
            index_book_two = shelf_with_books.index(book_two)
            shelf_with_books[index_book_one], shelf_with_books[index_book_two] =\
                shelf_with_books[index_book_two], shelf_with_books[index_book_one]
    elif command == "Insert Book":
        book_name = line[1]
        if book_name not in shelf_with_books:
            shelf_with_books.append(book_name)
    elif command == "Check Book":
        index = int(line[1])
        if index >= 0 and index < len(shelf_with_books):
            print(shelf_with_books[index])

    line = input()

print(", ".join(shelf_with_books))