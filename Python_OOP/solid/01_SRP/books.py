class Library:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def find_book(current_title):
        return current_title

    def __repr__(self):
        return f"This is the book: {self.find_book(current_title)}"


class Book(Library):
    def __init__(self, title):
        super().__init__(title)


book = Book("The moment I met you.")
print(Library.find_book(book))
