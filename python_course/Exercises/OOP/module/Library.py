# Library class that takes a dictionary of books as initial arguments
class Library:
    def __init__(self, catalog):
        self.catalog = catalog
    # method to print the catalog
    def __str__(self):
        return f"The books in the catalog are: {self.catalog}"
        
    # method to add a book given as a method argument 
    def add_book(self, book):
        isbn = book.isbn
        self.catalog[isbn] = [book.title, book.author]
        
    # method to remove a book given as a method argument 
    def remove_book(self, book):
        isbn = book.isbn
        if isbn in self.catalog:
            del self.catalog[isbn]
        else:
            return False
            
    # method to search for a book by title or author
    def search_by_title(self, title):
        list_search = []
        for isbn, info in self.catalog.items():
            if info[0] == title or info[1] == title:
                list_search.append((isbn, info))
                
        return list_search
    