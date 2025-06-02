# all user-define exceptions used in 'User' class
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

    # function to borrow book from the library
    def borrow_book(self, book_id, library):

        try:

            # when user already have books >= 3
            if len(self.borrowed_books) >= 3:
                raise MaxBooksLimitError("Cannot borrow more than 3 books.")

            # when book is already borrowed by u=the user
            if book_id in self.borrowed_
                books:
                raise AlreadyBorrowedError("Book already borrowed.")

            # finding book in the library
            book = library.get_book_by_id(book_id)

            # if the book is not found in the library
            if not book:
                raise BookNotFoundError("Book not found.")

            # if the book is not available right now, i.e. its quantity is 0
            if book.quantity == 0:
                raise BookUnavailableError("Book is not available right now.")

            # if there is none of the above errors, then book is borrowed by the user
            self.borrowed_books.append(book_id)
            library.mark_as_borrowed_book(book_id)
            return f"You have borrowed the book"

        except (MaxBooksLimitError, AlreadyBorrowedError, BookNotFoundError, BookUnavailableError) as e:
            return str(e)

    # function to return book to the library
    def return_book(self, book_id, library):
        try:
            # if book is not borrowed by the user
            if book_id not in self.borrowed_books:
                raise BookNotBorrowedError("You haven't borrowed this book.")

            # if book is borrowed by the user, then it is returned to the library
            self.borrowed_books.remove(book_id)
            library.mark_as_returned_book(book_id)
            return f"You have returned book with ID {book_id}."

        except BookNotBorrowedError as e:
            return str(e)