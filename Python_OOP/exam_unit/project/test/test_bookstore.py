from unittest import TestCase

from project.bookstore import Bookstore


class BookStoreTest(TestCase):

    def test_init(self):
        books_limit = 10
        book_store = Bookstore(10)
        self.assertEqual(books_limit, book_store.books_limit)
        self.assertDictEqual({}, book_store.availability_in_store_by_book_titles)
        self.assertEqual(0, book_store._Bookstore__total_sold_books)

    def test_books_limit_prop_correct(self):
        book_store = Bookstore(10)
        book_store.books_limit -= 1
        self.assertEqual(9, book_store.books_limit)

    def test_books_limit_prop_raise(self):
        book_store = Bookstore(10)
        with self.assertRaises(ValueError) as error:
            book_store.books_limit = -1
        self.assertEqual(f"Books limit of {-1} is not valid", str(error.exception))

    def test_len_is_correct(self):
        pass

    def test_len_if_is_not_correct(self):
        pass

    def test_receive_book_if_there_is_not_enough_space_in_the_bookstore(self):
        pass

    def test_receive_book_if_there_is_enough_space_in_the_bookstore(self):
        pass

    def test_receive_book_take_the_new_availability_of_that_book_copies_and_return_the_result(self):
        pass

    def test_sell_book_if_the_book_is_not_available_in_the_bookstore(self):
        pass

    def test_sell_book_if_there_is_not_enough_copies_of_that_book_to_sell(self):
        pass

    def test_sell_book_if_can_sell_successfully(self):
        pass

    def test_str(self):
        book_store = Bookstore(10)
        result = str(book_store)
        expected_result = str(book_store)
        self.assertEqual(expected_result, result)
