class BookNotFoundError(Exception):
    pass

class BookUnavailableError(Exception):
    pass

class MaxBooksLimitError(Exception):
    pass

class AlreadyBorrowedError(Exception):
    pass

class BookNotBorrowedError(Exception):
    pass


class User:
    def __init__(self, id, name, borrowed_books=None):
        self.id = id
        self.name = name
        self.borrowed_books = borrowed_books if borrowed_books else []

    def borrow_book(self, book_id, library):
        try:
            if len(self.borrowed_books) >= 3:
                raise MaxBooksLimitError("Cannot borrow more than 3 books.")

            if book_id in self.borrowed_books:
                raise AlreadyBorrowedError("Book already borrowed.")

            book = library.get_book_by_id(book_id)
            if not book:
                raise BookNotFoundError("Book not found.")

            if book.quantity <= 0:
                raise BookUnavailableError("Book is not available right now.")

            self.borrowed_books.append(book_id)
            library.mark_as_borrowed_book(book_id)
            return f"You have borrowed the book"

        except (MaxBooksLimitError, AlreadyBorrowedError, BookNotFoundError, BookUnavailableError) as e:
            return str(e)

    def return_book(self, book_id, library):
        try:
            if book_id not in self.borrowed_books:
                raise BookNotBorrowedError("You haven't borrowed this book.")

            self.borrowed_books.remove(book_id)
            library.mark_as_returned_book(book_id)
            return f"You have returned book with ID {book_id}."

        except BookNotBorrowedError as e:
            return str(e)