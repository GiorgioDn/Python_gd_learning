# Book class that requires title, author, isbn
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    # Method that overrides __str__ to print the description
    def __str__(self):
        return f"The book {self.title}, written by {self.author}, has the following ISBN code: {self.isbn}"