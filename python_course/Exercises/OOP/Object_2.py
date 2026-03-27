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

while True: 
    # input data to instantiate the class
    print("Enter the book author, title, and pages")
    title = input("Title: ")
    author = input("Author: ")
    pages = int(input("Pages: "))
    
    book = Book(title, author, pages)
    
    # use the __str__ method
    print(book)

    choice = input("Do you want to repeat the choice? ")
    
    # exit while loop
    if choice.lower() == "no":
        break