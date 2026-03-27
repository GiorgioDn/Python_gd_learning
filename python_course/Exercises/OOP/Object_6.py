from .module.Book import Book
from .module.Library import Library

catalog = {}

book_1 = Book("Me", "Author Name", 12334423232)

print(book_1)

book_2 = Book("Me 2.0", "Another Author", 12333423232)

catalog[book_1.isbn] = [book_1.title, book_1.author]

library = Library(catalog)

print(library)