# Import required classes from local modules
from models import Book
from models import Library
from models import User
from models import BookNotFoundError, UserNotFoundError


# Import environment variable handling libraries
from dotenv import load_dotenv
import os

# Load configuration from .env file and get admin password
load_dotenv()
password = os.getenv("ADMIN_PASSWORD")


def admin_menu():
    """
    Administrator menu providing complete library management functionality.
    Includes options for adding/removing books and users, and searching books.
    """

    # Define file paths
    books_file = "data/books.json"
    users_file = "data/users.json"

    library_instance = Library(books_file, users_file)
    
    while True:
        # Display menu options
        print("\nEnter your choice:\n1. Add book\n2. Add user\n3. Remove book\n4. Remove user\n5. Search book\n6. Exit\n")
        
        try:
            choice = int(input())
        except ValueError:
            print("Please enter a valid number!")
            continue

        # Handle different menu options using match-case
        match choice:

            case 1:
            # Add new book
                try:
                    # Collect book details from admin
                    book_id = input("Enter book id: ")
                    title = input("Enter title: ")
                    author = input("Enter author: ")
                    quantity = int(input("Enter no. of copies: "))

                    # Create and add new book
                    new_book = Book(book_id, title, author, quantity)
                    library_instance.add_book(new_book)

                except ValueError:
                    print("Invalid input.")

            case 2:
            # Add new user
                try:
                    # Collect user details
                    user_id = input("Enter user id: ")
                    name = input("Enter name: ")
                    borrowed_books = []  # Initialize empty borrowed books list
                    # Create and add new user
                    new_user = User(user_id, name, borrowed_books)
                    library_instance.add_user(new_user)

                except ValueError:
                    print("Invalid input.")

            case 3:
                # Remove book
                try:
                    book_id = input("Enter book id: ")

                    # First check if book exists
                    try:
                        quantity = library_instance.get_book_quantity(book_id)
                    except BookNotFoundError:
                        print(f"Error: Book with ID {book_id} does not exist in the library!")
                        continue

                    if quantity == 0:
                        print(f"Book with ID {book_id} has no copies available!")
                    else:
                        print(f"Current quantity: {quantity}")
                        print("Want to remove all copies?, if yes enter 'all' else enter quantity")
                        copies = input()

                        if copies.lower() == "all":
                            print(library_instance.remove_book(book_id))
                        else:
                            try:
                                quantity_to_remove = int(copies)
                                if quantity_to_remove <= quantity:
                                    library_instance.remove_book_copies(book_id, quantity_to_remove)
                                    print(f"{quantity_to_remove} copies of book with ID {book_id} removed.")
                                else:
                                    print(
                                        f"Error: Cannot remove {quantity_to_remove} copies. Only {quantity} copies available.")
                            except ValueError:
                                print("Invalid quantity entered!")
                except BookNotFoundError as e:
                    print(f"Error: {e}")

            case 4:
                # Remove user
                print("Enter user id of the user to remove: ")
                user_id = input().strip()

                if not user_id:  # Check for empty input
                    print("Error: User ID cannot be empty!")
                    continue

                try:
                    result = library_instance.remove_user(user_id)
                    print(result)
                except UserNotFoundError as e:
                    print(f"Error: {e}")

            case 5:  # Search book
                try:
                    print("Want to search by author or title?")
                    search_by = int(input("Choose 1 for author or 2 for title: "))

                    # search by author
                    if search_by == 1:
                        print("Enter author name: ")
                        author = input()
                        print(library_instance.search_book_by_author(author))

                    # search by title
                    elif search_by == 2:
                        print("Enter title: ")
                        title = input()
                        # searching book by title
                        library_instance.search_book_by_title(title)

                    else:
                        print("Invalid choice!")

                except ValueError:
                    print("Invalid input.")

            case 6:  # Exit admin menu
                print("Exiting the library....")
                return

            case _:  # Handle invalid choices
                print("Invalid choice!")
            

def library_user_menu():
    """
    Regular user menu with limited functionality.
    Allows users to search, borrow, and return books.
    """
    # User logins
    user_id= input("Enter your user_id")

    # Define file paths
    books_file = "data/books.json"
    users_file = "data/users.json"

    library_instance = Library(books_file, users_file)
    user = library_instance.get_user_by_id(user_id)

    if user is None:
        print("User does not exist.")
        return

    while True:
        # Display user menu options
        print("Enter your choice:\n1. Search book in library\n2. Borrow book\n3. Return book\n4. Exit\n")
        choice = int(input())

        match choice:
            case 1:  # Search book
                print("Want to search by author or title?")
                search_by = int(input("Choose 1 for author or 2 for title: "))

                # Handle search by author or title
                if search_by == 1:
                    print("Enter author name: ")
                    author = input()
                    print(library_instance.search_book_by_author(author))

                elif search_by == 2:
                    print("Enter title: ")
                    title = input()
                    print(library_instance.search_book_by_title(title))

                else:
                    print("Invalid choice!")

            case 2:  # Borrow book
                print("Enter book id: ")
                book_id = input()
                print(user.borrow_book(book_id, library_instance))

            case 3:  # Return book
                print("Enter book id: ")
                book_id = input()
                # Check if return is successful and update library records
                print(user.return_book(book_id, library_instance))

            case 4:  # Exit user menu
                print("Exiting the library....")
                return

            case _:  # Handle invalid choices
                print("Invalid choice!")

def main():
    """
    Main function that serves as the entry point of the library system.
    Handles user type selection and authentication.
    """
    # Define file paths
    books_file = "data/books.json"
    users_file = "data/users.json"

    library_instance = Library(books_file, users_file)

    # Display welcome message and get user type
    print("\nWelcome to the Library Book Borrowing System")
    print("Enter who are you?\n1. Admin\n2. Library user\n")
    user = int(input())

    # Handle admin login with password authentication
    if user == 1:
        entered_password = input("Enter password:")
        if entered_password == password:
            print("Welcome admin!")
            admin_menu()
        else:
            print("Wrong password.")

    # Handle regular user access
    elif user == 2:
        library_user_menu()

    # Handle invalid user type
    else: 
        print("Wrong input!")


# Program entry point
if __name__ == "__main__":
    main()