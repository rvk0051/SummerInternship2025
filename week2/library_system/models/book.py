class Book:
    # Each book has 4 attributes: id, title, author, and quantity.
    def __init__(self, id, title, author, quantity):
        self.id = id
        self.title = title
        self.author = author
        self.quantity = quantity

    # displaying info of book
    def display_info(self):
        return (f"book-id: {self.id}:\n{self.title} by {self.author}\n"
                f"Quantity: {self.quantity}")