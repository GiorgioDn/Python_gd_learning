# define the Book class
class Book: 
    # constructor with title, author, pages
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    # method to customize string representation
    def __str__(self):
        return f"The book {self.title} was written by {self.author} and has {self.pages} pages"

# define the Library class
class Library: 

    def __init__(self):
        self.book_list = []
        
    def add_book(self, title, author, pages):
        book = Book(title, author, pages)
        self.book_list.append([title, author, pages])
        print(book)
    def __str__(self):
        return f"The library has the following books: {self.book_list}"
    
library = Library()

while True: 
    # input data to instantiate the class
    print("Enter the author, title, and pages of the book to add to the library")
    title = input("Title: ")
    author = input("Author: ")
    pages = int(input("Pages: "))
     
    library.add_book(title, author, pages)
    
    print(library)

    choice = input("Do you want to repeat the choice? ")
    
    # exit while loop
    if choice.lower() == "no":
        break