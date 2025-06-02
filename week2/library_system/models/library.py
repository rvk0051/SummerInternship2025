from  models import Book
from  models import User
from utils.file_handler import load_data, save_data


class BookNotFoundError(Exception):
    pass

class UserNotFoundError(Exception):
    pass


class Library:
    def __init__(self, books_file, users_file):
        self.books_file = books_file
        self.users_file = users_file
        self.books = [Book(**book) for book in load_data(books_file)]
        self.users = [User(**user) for user in load_data(users_file)]

    def add_book(self, new_book):
        # function for adding book to library
        # called in 'main' function
        # if book already present in library, then increment its quantity

        for book in self.books:
            if book.title == new_book.title and book.author == new_book.author:
                book.quantity += new_book.quantity
                self.save_book()
                return
            if book.id == new_book.id:
                print("A book with same id already exists. Please enter a different id.")
                return

        # if book not present in library, then adding it to library
        self.books.append(new_book)
        self.save_book()
        print(f"Book {new_book.title} added successfully!")

    def add_user(self, user):
        # Adding user to library
        # called in 'main' function
        for user in self.users:
            if user.id == user.id:
                print("A user with same id already exists. Please enter a different id.")
                return
        self.users.append(user)
        self.save_user()
        print(f"User {user.name} added successfully!")

    def get_book_quantity(self, book_id):
        # Getting book quantity
        # called in case3 of 'main' function in main.py
        for book in self.books:
            if book.id == book_id:
                return book.quantity

        raise BookNotFoundError("Book not found!")

    def get_book_by_id(self, book_id):
        # getting book by it's id
        # called in 'borrow_book' function of 'User' class'
        for book in self.books:
            if book.id == book_id:
                return book
        raise BookNotFoundError("Book not found!")

    def get_user_by_id(self, user_id):
        # getting user by it's id
        # called when user logins
        for user in self.users:
            if user.id == user_id:
                return user
        raise UserNotFoundError("User not found!")

    def mark_as_borrowed_book(self, book_id):
        # marking book as borrowed
        # this function is called by 'borrow_book' function of 'User' class
        for book in self.books:
            if book.id == book_id:
                book.quantity -= 1
                self.save_book()
                return
        raise BookNotFoundError("Book not found!")

    def mark_as_returned_book(self, book_id):
        # marking book as returned
        # this function is called by 'return_book' function of 'User' class
        for book in self.books:
            if book.id == book_id:
                book.quantity += 1
                self.save_book()

    def remove_book_copies(self, book_id, copies):
        # removing specific number of copies of book from the library
        # function called by 'case3' of 'admin_menu' function in 'main.py'
        for book in self.books:
            if book.id == book_id:
                if book.quantity > copies:
                    book.quantity -= copies
                    self.save_book()
                    return f"{copies} copies of book {book_id} removed"
                else:
                    self.remove_book(book_id)
                    return "All copies of books removed"
        raise BookNotFoundError("Book not found!")

    def remove_book(self, book_id):
        # removing all copies of book from the library
        # function called by 'case3' of 'admin_menu' function in 'main.py'
        prev_books = self.books
        self.books = [book for book in self.books if book.id != book_id]
        if self.books == prev_books:
            raise BookNotFoundError("Book not found!")
        else:
            self.save_book()
            return "Book removed successfully!"

    def remove_user(self, user_id):
        # removes user from the library
        # # function called by 'case4' of 'admin_menu' function in 'main.py'
        prev_users = self.users
        self.users = [user for user in self.users if user.id != user_id]
        if self.users == prev_users:
            raise UserNotFoundError("User not found")
        else:
            self.save_user()
            return "User removed successfully!"

    def search_book_by_author(self, book_author):
        # searching book by author
        # function called by 'case5' of 'admin_menu' function in 'main.py'
        found_books = [book for book in self.books if book.author == book_author]
        if found_books:
            for book in found_books:
                print(book.display_info())
        else:
            raise BookNotFoundError("Book not found!")

    def search_book_by_title(self, book_title):
        # searching book by title
        # function called by 'case5' of 'admin_menu' function in 'main.py'
        found_books = [book for book in self.books if book.title == book_title]
        if found_books:
            for book in found_books:
                print(book.display_info())
        else:
            raise BookNotFoundError("Book not found!")

    def save_book(self):
        # saving books to file
        # being called in the 'Library' functions itself
        save_data(self.books_file, [vars(book) for book in self.books])

    def save_user(self):
        # saving users to file
        # being called in the 'Library' functions itself
        save_data(self.users_file, [vars(user) for user in self.users])